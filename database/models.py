from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
import scrapy
from scrapy_djangoitem import DjangoItem

from scl.models import (
    BaseModel,
    ModerationBaseModel,
)


class KnowledgeBaseAbstractModel(BaseModel):
    title = models.CharField(
        _("Заголовок"),
        max_length=250)
    slug = models.SlugField(
        _("Слаг"))
    description = models.TextField(
        _("Описание"),
        blank=True)
    published = models.BooleanField(
        _("Опубликовано"),
        default=True,
        help_text=_("Если стоит галочка запись будет доступна на сайте."))


class Category(MPTTModel, BaseModel):
    """
    Категория в Базе Знаний, расширена
    MPTTModel и BaseModel, содержит
    поля title, slug, description,
    keywords, parent
    """
    title = models.CharField(
        _("Заголовок"),
        max_length=250)
    slug = models.SlugField(
        _("Слаг"))
    description = models.TextField(
        _("Описание"),
        blank=True)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Родитель'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    class MPTTMeta:
        order_insertion_by = ['title']


class Funding(models.Model):
    funds = models.IntegerField()
    fans = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class FundingItem(DjangoItem):
    django_model = Funding
    success = scrapy.Field(default=False)


class Company(KnowledgeBaseAbstractModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Катерогия"))
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


class Ship(KnowledgeBaseAbstractModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Катерогия"))
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
