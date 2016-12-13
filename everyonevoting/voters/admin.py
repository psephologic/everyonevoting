__author__ = 'eronlloyd'

from django.contrib import admin

from .models import Affiliation, VoterRegistration, RegistryImport


@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):
    pass

@admin.register(VoterRegistration)
class VoterRegistrationAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')



@admin.register(RegistryImport)
class RegistryImportAdmin(admin.ModelAdmin):
    pass
