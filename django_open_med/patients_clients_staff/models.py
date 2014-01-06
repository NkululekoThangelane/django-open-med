from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User)
    org = models.OneToOneField('organization.Organization')
class PersonProfile(models.Model):
    user = models.OneToOneField(User)
    org =  models.OneToOneField('organization.Organization')
class Patient(Person):
    pass

class Client(Person):
    pass

class Guardian(Person):
    pass
class Employee(Person):
    pass
class Physician(Person):
    pass
class Therapist(Person):
    pass
class EmployerData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    street = models.CharField()
    postal_code = models.CharField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    assoc_id = models.ForeignKey()

class HistoryData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(editable=False,auto_now=True)
    assoc_id =
    coffee
    tobacco
    alcohol
    sleep_patterns
    exercist_patterns
    seatbelt_use
    counseling
    harzardous_activities
    last_breast_exam
    last_mammogram
    last_gynocological_exam
    last_rectal_exam
    last_prostate_exam
    last_sigmoidoscopy_colonoscopy
    history_mother
    history_father
    history_siblings
    history_offspring
    history_spouse
    relatives_cancer
    relatives_tuberculosis
    relatives_diabetes
    relatives_high_blood_pressure
    relatives_heart_problems
    relatives_stroke
    relatives_epilepsy
    relatives_mental_illness
    relatives_suicide
    catarct_surgery
    tonsillectomy
    cholecystestomy
    heart_surgery
    hysterectomy
    hernia_repair
    hip_replacement
    knee_replacement
    appendectomy=

class Immunization(models.Model):
