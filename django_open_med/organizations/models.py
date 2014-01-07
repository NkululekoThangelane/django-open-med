from django.conf import settings
from django.db import models
from django.db.models import permalink, get_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from organizations.managers import OrgManager, ActiveOrgManager


class Organization(TimeStampedModel):
    """
    The umbrella object with which users can be associated.

    An organization can have multiple users but only one who can be designated
    the owner user.

    """
    name = models.CharField(max_length=200,
            help_text=_("The name of the organization"))
    slug = AutoSlugField(max_length=200, blank=False, editable=True,
            populate_from='name', unique=True,
            help_text=_("The name in all lowercase, suitable for URL identification"))
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    address = models.ForeignKey('users.Address')

    objects = OrgManager()
    active = ActiveOrgManager()

    class Meta:
        ordering = ['name']
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")

    def __str__(self):
        return u"{0}".format(self.name)

    @permalink
    def get_absolute_url(self):
        return ('organization_detail', (), {'organization_pk': self.pk})

    def add_user(self, user, is_admin=False):
        """
        Adds a new user and if the first user makes the user an admin and
        the owner.
        """
        users_count = self.users.all().count()
        if users_count == 0:
            is_admin = True
        org_user = User.objects.create(user=user,
                organization=self, is_admin=is_admin)
        if users_count == 0:
            OrganizationOwner.objects.create(organization=self,
                    organization_user=org_user)
        return org_user

    def get_or_add_user(self, user, is_admin=False):
        """
        Adds a new user to the organization, and if it's the first user makes
        the user an admin and the owner. Uses the `get_or_create` method to
        create or return the existing user.

        `user` should be a user instance, e.g. `auth.User`.

        Returns the same tuple as the `get_or_create` method, the
        `OrganizationUser` and a boolean value indicating whether the
        OrganizationUser was created or not.
        """
        users_count = self.users.all().count()
        if users_count == 0:
            is_admin = True

        org_user, created = settings.AUTH_USER_MODEL.objects.get_or_create(
                organization=self, user=user, defaults={'is_admin': is_admin})

        if users_count == 0:
            OrganizationOwner.objects.create(organization=self,
                    organization_user=org_user)

        return org_user, created

    def is_member(self, user):
        return True if user in self.users.all() else False

    def is_admin(self, user):
        return True if self.organization_users.filter(user=user, is_admin=True) else False

class OrganizationOwner(TimeStampedModel):
    """Each organization must have one and only one organization owner."""

    organization = models.OneToOneField(Organization, related_name="owner")
    organization_user = models.OneToOneField(settings.AUTH_USER_MODEL,
            related_name="owned_organization")

    class Meta:
        verbose_name = _("organization owner")
        verbose_name_plural = _("organization owners")

    def __str__(self):
        return u"{0}: {1}".format(self.organization, self.organization_user)

    def save(self, *args, **kwargs):
        """
        Extends the default save method by verifying that the chosen
        organization user is associated with the organization.

        """
        from organizations.exceptions import OrganizationMismatch
        if self.organization_user.organization != self.organization:
            raise OrganizationMismatch
        else:
            super(OrganizationOwner, self).save(*args, **kwargs)
