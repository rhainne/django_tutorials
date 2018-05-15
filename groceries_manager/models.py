import datetime 

from django.db import models
from django.utils import timezone


class Product_category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Product_group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Product_subgroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2)
    name = models.CharField(max_length=200)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    id_supermarket = models.IntegerField(default=1)
    date = models.DateTimeField('Bought on this day')


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.IntegerField(default=None)
    group = models.IntegerField(default=None)
    subgroup = models.IntegerField(default=None)


class Ticket_line(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    unit_price = models.FloatField(default=None)
    quantity = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)


class Supermarket(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=50)
    franchise = models.CharField(max_length=50)
    name = models.CharField(max_length=200)


