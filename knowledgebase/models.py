from django.db import models
from django.utils.translation import ugettext_lazy as _
import scrapy
from scrapy_djangoitem import DjangoItem

from scl.models import BaseModel


class CommonPage(BaseModel):
    title = models.CharField(
        _("Заголовок"),
        max_length=250)
    slug = models.SlugField(
        _("Слаг"),
        max_length=250)
    content = models.TextField(
        _('Контент'),
        blank=True)
    description = models.TextField(
        _("Описание"),
        blank=True)
    published = models.BooleanField(
        _("Опубликовано"),
        default=True,
        help_text=_("Если стоит галочка запись будет доступна на сайте."))

    class Meta:
        abstract = True


class Page(CommonPage):
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Funding(models.Model):
    funds = models.IntegerField()
    fans = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.funds


class FundingItem(DjangoItem):
    django_model = Funding
    success = scrapy.Field(default=False)


class Company(CommonPage):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    race = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    current_ceo = models.CharField(max_length=255, blank=True)
    founder = models.CharField(max_length=255, blank=True)
    founded = models.CharField(max_length=255, blank=True)
    demographic = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class CompanyItem(DjangoItem):
    django_model = Company
    success = scrapy.Field(default=False)


class Ship(CommonPage):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    manufacturer = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    focus = models.CharField(max_length=255, blank=True)
    prod_state = models.CharField(max_length=255, blank=True)
    max_crew = models.CharField(max_length=255, blank=True)
    cargo_capacity = models.CharField(max_length=255, blank=True)
    rec_cost = models.CharField(max_length=255, blank=True)
    pledge_cost = models.CharField(max_length=255, blank=True)
    null_cargo_mass = models.CharField(max_length=255, blank=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    beam = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ShipItem(DjangoItem):
    django_model = Ship
    success = scrapy.Field(default=False)
