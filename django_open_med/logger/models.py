from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
TYPE_CHOICES = (
    ('C', 'CREATE'),
    ('G', 'GET'),
    ('L', 'LIST'),
    ('U', 'UPDATE'),
    ('D', 'DELETE'),
    ('E', 'ERROR'),

)

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(editable=False,auto_now=True)
    event_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='E')
    event = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    org = models.ForeignKey('organizations.Organization')
    comments = models.TextField()

