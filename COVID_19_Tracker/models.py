# Create your models here.
from django.db import models
from django.utils import timezone
class Global(models.Model):
    gid=models.CharField(max_length=100000, unique=True)
    newConfirmed= models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths=models.IntegerField()
    totalDeaths=models.IntegerField()
    newRecovered=models.IntegerField()
    totalRecoverd=models.BigIntegerField()
    date=models.DateTimeField(auto_now_add=True)


class Countries(models.Model):
    cid=models.CharField(max_length=10000,unique=True)
    country=models.CharField(max_length=1000)
    countryCode=models.CharField(max_length=100)
    slugId=models.SlugField(unique=True)
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    newRecovered = models.IntegerField()
    totalRecoverd = models.BigIntegerField()
    date=models.DateTimeField()

    def __str__(self):
        return self.country
