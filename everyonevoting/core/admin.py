from django.contrib import admin

from core.models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ["organization_name"]
    readonly_fields = ('date_created', 'date_updated')