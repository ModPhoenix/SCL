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


class Ship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    manufacturer = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )
    focus = models.CharField(max_length=60)
    prod_state = models.CharField(max_length=60)
    max_crew = models.IntegerField()
    rec_cost = models.IntegerField()
    pledge_cost = models.IntegerField()
