from django.db import models

# Create your models here.
class InsuranceData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(editable=False,auto_now=True)
    assoc_id
    insurance_type
    provider
    policy_number
    group_number
    subscriber = models.ForeignKey()
    subscriber_relationship =
    subscriber_employer
    copay = 

class InsuranceCompany(models.Model):    
