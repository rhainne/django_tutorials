import datetime 

from django.db import models
from django.utils import timezone


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    supermarket_id = models.IntegerField(default=None)
    price = models.FloatField(default=None)
    weight = models.FloatField(default=None)
    units = models.IntegerField(default=None)
    price_per_unit = models.FloatField(default=None)
    price_per_kilo = models.FloatField(default=None)
    bought_on = models.DateTimeField('Bought on this day')
    

class Supermarket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

