from django.contrib import admin
from insurance.models import InsuranceData, InsuranceCompany
# Register your models here.
class InsuranceDataAdmin(admin.ModelAdmin):
    pass
class InsuranceCompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(InsuranceData, InsuranceDataAdmin)
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)
