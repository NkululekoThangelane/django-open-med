from django.contrib import admin
from organizations.models import (Organization,
        OrganizationOwner)


class OwnerInline(admin.StackedInline):
    model = OrganizationOwner
    raw_id_fields = ('organization_user',)


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    list_display = ['name', 'is_active']
    prepopulated_fields = {"slug": ("name",)}


class OrganizationOwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('organization_user', 'organization')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationOwner, OrganizationOwnerAdmin)
