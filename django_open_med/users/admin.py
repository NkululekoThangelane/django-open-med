from django.contrib import admin
from users.models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    pass
class ClientAdmin(admin.ModelAdmin):
    pass
class GuardianAdmin(admin.ModelAdmin):
    pass
class EmployeeAdmin(admin.ModelAdmin):
    pass
class PhysicianAdmin(admin.ModelAdmin):
    pass
class TherapistAdmin(admin.ModelAdmin):
    pass
class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Address, AddressAdmin)
