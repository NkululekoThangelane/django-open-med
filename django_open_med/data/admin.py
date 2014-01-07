from django.contrib import admin
from data.models import *
# Register your models here.
class EmployerDataAdmin(admin.ModelAdmin):
    pass
class ListAdmin(admin.ModelAdmin):
    pass
class HistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmployerData, EmployerDataAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(History, HistoryAdmin)
