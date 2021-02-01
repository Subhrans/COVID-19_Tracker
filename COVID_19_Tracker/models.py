# Create your models here.
from django.db import models


class Global(models.Model):
    gid = models.CharField(max_length=100000,null=True,blank=True)
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    newRecovered = models.IntegerField()
    totalRecoverd = models.BigIntegerField()
    update_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)



class Countries(models.Model):
    cid = models.CharField(max_length=10000, unique=True)
    country = models.CharField(max_length=1000)
    countryCode = models.CharField(max_length=100)
    slugId = models.SlugField()
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    newRecovered = models.IntegerField()
    totalRecoverd = models.BigIntegerField()
    lat=models.DecimalField(max_digits=20,decimal_places=10,blank=True,null=True)
    lon=models.DecimalField(max_digits=20,decimal_places=10,blank=True,null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.country


class CountriesHistory(models.Model):
    cid = models.CharField(max_length=10000, unique=True)
    country = models.CharField(max_length=1000)
    countryCode = models.CharField(max_length=100)
    slugId = models.SlugField()
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    newRecovered = models.IntegerField()
    totalRecoverd = models.BigIntegerField()
    date = models.DateTimeField()
    saved_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.date)


class India(models.Model):
    state=models.CharField(max_length=1000)
    state_code = models.CharField(max_length=100)
    active = models.BigIntegerField()
    confirmed = models.BigIntegerField()
    deaths = models.BigIntegerField()
    recovered = models.BigIntegerField()
    new_confirmed = models.BigIntegerField()
    new_deaths = models.BigIntegerField()
    new_recovered = models.BigIntegerField()
    last_update_time = models.DateTimeField()
    lat = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    lon = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class IndiaHistory(models.Model):
    state = models.CharField(max_length=1000)
    state_code = models.CharField(max_length=100)
    active = models.BigIntegerField()
    confirmed = models.BigIntegerField()
    deaths = models.BigIntegerField()
    recovered = models.BigIntegerField()
    new_confirmed = models.BigIntegerField()
    new_deaths = models.BigIntegerField()
    new_recovered = models.BigIntegerField()
    last_update_time = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)

class CountryCode(models.Model):
    iso=models.CharField(max_length=128)
    name=models.CharField(max_length=1000)
