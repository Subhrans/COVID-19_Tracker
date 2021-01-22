# Register your models here.
from django.contrib import admin

from .models import Global, Countries, CountriesHistory, India, IndiaHistory


@admin.register(Global)
class GlobalAdmin(admin.ModelAdmin):
    list_display = ['gid', 'date']


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['country', 'date','countryCode']
    search_fields = ['countryCode','country']


@admin.register(CountriesHistory)
class CountriesHistoryAdmin(admin.ModelAdmin):
    list_display = ['countryCode','country','saved_date', 'date']
    list_display_links = ['saved_date', 'country','countryCode','date']
    search_fields = ['countryCode', 'country']


@admin.register(India)
class IndiaAdmin(admin.ModelAdmin):
    list_display = ['state_code', 'last_update_time', 'creation_date']


@admin.register(IndiaHistory)
class IndiaHistoryAdmin(admin.ModelAdmin):
    list_display = ['state_code', 'last_update_time', 'creation_date']
