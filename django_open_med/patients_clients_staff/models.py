from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.db import models

from encrypted_fields import EncryptedCharField
from rest_framework.authtoken.models import Token
from autoslug import AutoSlugField

GENDER_CHOICES =(
    ('M', 'Male'),
    ('F', 'Female'),
)
# Create your models here.
class AppUser(AbstractUser):
    slug = models.AutoSlugField(populate_from='user', unique_with='user')
    org = models.OneToOneField('organization.Organization')
    token = models.ForeignKey(Token)
    class Meta:
        abstract = True

class Patient(AppUser):
    pass

class ClientManager(models.Manager):
    pass

class Client(AppUser):
   guardian = models.ForeignKey('Guardian', null=True, blank=True)
   guardian_relation = models.CharField(max_length=50, null=True,blank=True)
   gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
   ssn = EncryptedCharField(null=True)
   activated = _('ALREADY_ACTIVATED')
   dob = models.DateField()
   phone = models.CharField(max_length=15, null=True, blank=True)
   address = models.ForeignKey('Address')
   insurance = models.ForeignKey('insurance.InsuranceData',null=True,blank=True)
   employer = models.ForeignKey('data.EmployerData', null=True, blank=True)
   objects = ClientManager()

   def __unicode__(self):
       return '%s' % self.username

   class Meta:
       verbose_name_plural = "Clients"

class GuardianManager(models.Manager):
    pass

class Guardian(AppUser):
    activated = _('ALREADY_ACTIVATED')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.ForeignKey('Address')
    insurance = models.ForeignKey('insurance.InsuranceData',null=True, blank=True)
    employer = models.ForeignKey('data.EmployerData', null=True, blank=True)
    object = GuardianManager()

    def __unicode__(self):
        return '%s' % self.username

    class Meta:
        verbose_name_plural = "Guardians"

class EmployeeManager(models.Manager):
    pass

class Employee(AppUser):
    manager = models.BooleanField()
    #schedule = models.ForeignKey('schedule.Calendar')
    objects = EmployeeManager()

    def __unicode__(self):
        return '%s' % self.username

    class Meta:
        verbose_name_plural = "Employees"

class Physician(AppUser):
    pass
class Therapist(AppUser):
    pass
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.IntegerField()
