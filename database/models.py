from django.db import models
import scrapy
from scrapy_djangoitem import DjangoItem


class Funding(models.Model):
    funds = models.IntegerField()
    fans = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class FundingItem(DjangoItem):
    django_model = Funding
    success = scrapy.Field(default=False)


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

class CompanyItem(DjangoItem):
    django_model = Company
    success = scrapy.Field(default=False)

class Ship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    manufacturer = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    focus = models.CharField(max_length=60, blank=True, null=True)
    prod_state = models.CharField(max_length=60, blank=True, null=True)
    max_crew = models.IntegerField(blank=True, null=True)
    cargo_capacity = models.IntegerField(blank=True, null=True)
    rec_cost = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    pledge_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    null_cargo_mass = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

class ShipItem(DjangoItem):
    django_model = Ship
    success = scrapy.Field(default=False)