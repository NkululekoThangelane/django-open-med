from django.contrib import admin

from schedule.models import Calendar, CalendarRelation, Event

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Event, EventAdmin)
