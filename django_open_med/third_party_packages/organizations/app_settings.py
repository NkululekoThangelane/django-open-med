from django.conf import settings

from third_party_packages.organizations.utils import model_field_attr


ORGS_INVITATION_BACKEND = getattr(settings, 'INVITATION_BACKEND',
        'organizations.backends.defaults.InvitationBackend')

ORGS_REGISTRATION_BACKEND = getattr(settings, 'REGISTRATION_BACKEND',
        'organizations.backends.defaults.RegistrationBackend')

ORGS_EMAIL_LENGTH = model_field_attr(settings.AUTH_USER_MODEL, 'email', 'max_length')
