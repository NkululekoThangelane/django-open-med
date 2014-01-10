from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass
class PatientAdmin(UserAdmin):
    pass
class ClientAdmin(UserAdmin):
    pass
class GuardianAdmin(UserAdmin):
    pass
class EmployeeAdmin(UserAdmin):
    pass
class PhysicianAdmin(UserAdmin):
    pass
class TherapistAdmin(UserAdmin):
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
admin.site.register(CustomUser, CustomUserAdmin)
