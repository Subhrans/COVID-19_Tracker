# Register your models here.
from django.contrib import admin

from .models import Global, Countries, CountriesHistory, India, IndiaHistory,CountryCode


@admin.register(Global)
class GlobalAdmin(admin.ModelAdmin):
    list_display = ['gid', 'date','update_date']
    list_display_links = ['gid','date','update_date']
    search_fields = ['date']


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['country', 'date','countryCode']
    search_fields = ['countryCode','country','date']


@admin.register(CountriesHistory)
class CountriesHistoryAdmin(admin.ModelAdmin):
    list_display = ['countryCode','country','saved_date', 'date']
    list_display_links = ['saved_date', 'country','countryCode','date']
    search_fields = ['countryCode', 'country']


@admin.register(India)
class IndiaAdmin(admin.ModelAdmin):
    list_display = ['state_code', 'state','last_update_time', 'creation_date']


@admin.register(IndiaHistory)
class IndiaHistoryAdmin(admin.ModelAdmin):
    list_display = ['state_code', 'last_update_time', 'creation_date']

@admin.register(CountryCode)
class CountryCodeAdmin(admin.ModelAdmin):
    list_display = ['iso','name']
    search_fields = ['iso','name']
    list_filter = ['iso','name']