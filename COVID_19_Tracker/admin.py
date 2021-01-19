# Register your models here.
from django.contrib import admin
from .models import Global,Countries
@admin.register(Global)
class GlobalAdmin(admin.ModelAdmin):
    list_display = ['gid','date']

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['cid','date']