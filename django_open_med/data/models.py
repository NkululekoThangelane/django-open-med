from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from autoslug import AutoSlugField
# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    org = models.ForeignKey('organization.Organization')

    class Meta:
        abstract = True
class EmployerData(Data):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name')
    address = models.ForeignField('patients_clients_staff.Address')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = "Employer Data"

class List(Data):
    pass

class History(Data):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    patient = models.ForeignKey('patients_clients_staff.Patient')
    coffee = models.TextField()
    tobacco = models.TextField()
    alcohol = models.TextField()
    sleep_patterns = models.TextField()
    exercise_patterns = models.TextField()
    seatbelt_use = models.TextField()
    counseling = models.TextField()
    hazardous_activites = models.TextField()
    last_breast_exam = models.DateField(blank=True)
    last_mammogram = models.DateField(blank=True)
    last_gynocological_exam = models.DateField(blank=True)
    last_rectal_exam = models.DateField(blank=True)
    last_prostate_exam = models.DateField(blank=True)
    last_sigmoidoscopy_colonoscopy = models.DateField(blank=True)
    history_mother = models.TextField()
    history_father = models.TextField()
    history_siblings = models.TextField()
    history_offspring = models.TextField()
    history_spouse= models.TextField()
    relatives_tb = models.TextField()
    relatives_diabetes = models.TextField()
    relatives_hbp = models.TextField()
    relatives_heart_problems = models.TextField()
    relatives_stroke = models.TextField()
    relatives_epilepsy = models.TextField()
    relatives_mental_illness = models.TextField()
    relatives_suicide = models.TextField()
    cataract_surgery = models.BooleanField()
    tonsillectomy = models.BooleanField()
    cholecystestomy = models.BooleanField()
    heart_surgery = models.BooleanField()
    hysterectomy = models.BooleanField()
    hernia_repair = models.BooleanField()
    hip_replacement = models.BooleanField()
    knee_replacement = models.BooleanField()
    appendectomy = models.BooleanField()
