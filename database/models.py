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
