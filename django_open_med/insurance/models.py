from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.
class InsuranceBase(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    timestamp = models.DateTimeField(editable=False,auto_now=True)

class InsuranceData(InsuranceBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    provider = models.ForeignKey('InsuranceCompany')
    policy_number = models.CharField(max_length=255)
    group_number = models.CharField(max_length=255)
    subscriber_data = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriber_data')
    copay = models.DecimalField(max_digits=10, decimal_places=2)

class InsuranceCompany(InsuranceBase):
    name = models.CharField(max_length=255)
    address = models.ForeignKey('users.Address')
