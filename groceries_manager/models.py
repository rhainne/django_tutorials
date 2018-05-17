import datetime 

from django.db import models
from django.utils import timezone


class Product_category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return self.name


class Product_group(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(Product_category, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Product group'
        verbose_name_plural = 'Product groups'

    def __str__(self):
        return self.name


class Product_subgroup(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(Product_category, on_delete=models.CASCADE, default=None)
    id_group = models.ForeignKey(Product_group, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Product subgroup'
        verbose_name_plural = 'Product subgroups'

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Supermarket(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=50)
    franchise = models.CharField(max_length=50)
    name = models.CharField('Supermarket', max_length=200)

    class Meta:
        verbose_name = 'Supermarket'
        verbose_name_plural = 'Supermarkets'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    id_supermarket = models.ForeignKey(Supermarket, db_column = 'id_supermarket', on_delete=models.CASCADE)
    date = models.DateTimeField('Bought on this day')

    def __str__(self):
        return "id: {0}, supermarket: {1}, date: {2}."\
                .format(self.id, self.id_supermarket, self.date)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    group = models.ForeignKey(Product_group, on_delete=models.CASCADE)
    subgroup = models.ForeignKey(Product_subgroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ticket_line(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    unit_price = models.FloatField(default=None)
    quantity = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return "ticket_line_id: {0}, product: {1}, ticket_id: {2}, unit price: {3}, quantity: {4}"\
                .format(self.id, self.id_product, self.id_ticket, self.unit_price, self.quantity)