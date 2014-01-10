from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings
from encrypted_fields import EncryptedCharField
from autoslug import AutoSlugField

GENDER_CHOICES =(
    ('M', 'Male'),
    ('F', 'Female'),
)
# Create your models here.
class CustomUser(AbstractUser):
    slug = AutoSlugField(populate_from='username', unique_with='username')
    org = models.ForeignKey('organizations.Organization', null=True)
    objects = UserManager()

    def __unicode__(self):
        return '%s' % self.first_name + ' ' + self.last_name
    class Meta(AbstractUser.Meta):
        db_table= "auth_user"
class Patient(CustomUser):
    doctor = models.ForeignKey('Physician')

    class Meta:
        verbose_name_plural = "Patients"

class ClientManager(models.Manager):
    pass

class Client(CustomUser):
   guardian = models.ForeignKey('Guardian', null=True, blank=True)
   guardian_relation = models.CharField(max_length=50, null=True,blank=True)
   gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
   ssn = EncryptedCharField(max_length=25,null=True)
   activated = _('ALREADY_ACTIVATED')
   dob = models.DateField()
   phone = models.CharField(max_length=15, null=True, blank=True)
   address = models.ForeignKey('Address')
   insurance = models.ForeignKey('insurance.InsuranceData',null=True,blank=True, related_name='client_insurance')
   employer = models.ForeignKey('data.EmployerData', null=True, blank=True)
   objects = ClientManager()

   def __unicode__(self):
       return '%s' % self.username

   class Meta:
       verbose_name_plural = "Clients"

class GuardianManager(models.Manager):
    pass

class Guardian(CustomUser):
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

class Employee(CustomUser):
    manager = models.BooleanField(default=False)
    #schedule = models.ForeignKey('schedule.Calendar')
    objects = EmployeeManager()

    def __unicode__(self):
        return '%s' % self.username

    class Meta:
        verbose_name_plural = "Employees"

class Physician(CustomUser):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Physicians'
class Therapist(CustomUser):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Therapists'
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.IntegerField()
