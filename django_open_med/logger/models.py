from django.db import models

# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(editable=False,auto_now=True)
    event = 
    user = models.ForeignKey(User)
    organization = models.ForeignKey('organization.Organization')
    comments = models.CharField()
    
