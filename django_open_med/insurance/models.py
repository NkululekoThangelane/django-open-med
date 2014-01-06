from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.
class InsuranceData(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    timestamp = models.DateTimeField(editable=False,auto_now=True)
    user = models.OneToOneField(User)
    provider = models.ForeignKey('InsuranceCompany')
    policy_number = models.CharField(max_length=255)
    group_number = models.CharField(max_length=255)
    subscriber = models.ForeignKey(User)
    copay = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.FileField(blank=True)

class InsuranceCompany(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    timestamp = models.DateTimeField(editable=False, auto_now=True)
    name = models.CharField(max_length=255)
    address = models.ForeignKey('patients_clients_staff.Address')
