# Register your models here.
from django.contrib import admin
from .models import Global,Countries,CountriesHistory
@admin.register(Global)
class GlobalAdmin(admin.ModelAdmin):
    list_display = ['gid','date']

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['cid','date']

@admin.register(CountriesHistory)
class CountriesHistoryAdmin(admin.ModelAdmin):
    list_display = ['saved_date','date']
    list_display_links = ['saved_date','date']