from django.db import models
from simple_history.models import HistoricalRecords
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
    industry = models.CharField(max_length=80, blank=True, null=True)
    race = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    current_ceo = models.CharField(max_length=50, blank=True, null=True)
    founder = models.CharField(max_length=50, blank=True, null=True)
    founded = models.CharField(max_length=50, blank=True, null=True)
    demographic = models.CharField(max_length=50, blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class CompanyItem(DjangoItem):
    django_model = Company
    success = scrapy.Field(default=False)


class Ship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    manufacturer = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    # focus = models.CharField(max_length=60, blank=True, null=True)
    prod_state = models.CharField(max_length=60, blank=True, null=True)
    max_crew = models.SmallIntegerField(blank=True, null=True)
    cargo_capacity = models.IntegerField(blank=True, null=True)
    rec_cost = models.IntegerField(blank=True, null=True)
    pledge_cost = models.IntegerField(blank=True, null=True)
    null_cargo_mass = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    beam = models.FloatField(blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ShipItem(DjangoItem):
    django_model = Ship
    success = scrapy.Field(default=False)


''' 
/////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.utils.translation import to_locale, get_language, ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from scl.models import (
    BaseModel,
    ModerationBaseModel,
)


class Category(MPTTModel, ModerationBaseModel):
    """
    Category of item
    extend ItemBaseModel
    which has slug, name,
    description, keywords
    """
    slug = models.CharField(
        _("Slug"),
        default="",
        unique=True,
        max_length=250)
    name = models.CharField(
        _("Name"),
        default="",
        max_length=250)
    url = models.CharField(
        _("Scrapy Url"),
        default="",
        blank=True,
        max_length=250)
    title = models.CharField(
        _("Title"),
        blank=True,
        default="",
        max_length=250)
    description = models.CharField(
        _("Description"),
        blank=True,
        default="",
        max_length=250)
    keywords = models.CharField(
        _("Keywords"),
        blank=True,
        default="",
        max_length=250)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Parent'))
    image = models.ImageField(
        upload_to='category_images/',
        blank=True,
        default="",
        verbose_name=_('Image'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['name']


class Item(ModerationBaseModel):
    slug = models.CharField(
        _("Slug"),
        default="",
        blank=True,
        db_index=True,
        max_length=250)
    url = models.CharField(
        _("Url"),
        default="",
        blank=True,
        max_length=250)
    name = models.CharField(
        _("Name"),
        default="",
        max_length=250)
    sky = models.CharField(
        _("Sky"),
        blank=True,
        default="",
        db_index=True,
        max_length=250)
    title = models.CharField(
        _("Title"),
        blank=True,
        default="",
        max_length=250)
    description = models.CharField(
        _("Description"),
        blank=True,
        default="",
        max_length=250)
    keywords = models.CharField(
        _("Keywords"),
        blank=True,
        default="",
        max_length=250)
    image = models.ImageField(
        upload_to='Itemimeges/',
        blank=True,
        default="",
        verbose_name=_('Image'))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories',
        blank=True,
        null=True,
        verbose_name=_('Category'))
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name=_('Price'))
    promo = models.BooleanField(
        _(u'Published'),
        default=False,
        help_text=_('Show this Item on Home page?'))
    description = models.TextField(blank=True,)
    full_text = models.TextField(blank=True,)

    def save(self, *args, **kwargs):
        if self.category:
            super(Item, self).save(*args, **kwargs)
            # we create properties if not exist
            for cp in CategoryProperty.objects.filter(category=self.category):
                pp = ItemProperty.objects.filter(category_property=cp,
                                                 Item=self)
                if not pp:
                    pp = ItemProperty(category_property=cp,
                                      Item=self, value="--")
                    pp.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')


class CategoryProperty(ModerationBaseModel):
    name = models.CharField(
        _("Name"),
        default="",
        max_length=250)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='categories_property',
        verbose_name=_('Category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category property')
        verbose_name_plural = _('Category properties')


class ItemProperty(ModerationBaseModel):
    category_property = models.ForeignKey(
        CategoryProperty,
        on_delete=models.CASCADE,
        related_name='category_property',
        verbose_name=_('Propery'))
    value = models.CharField(
        _("Value"),
        default="",
        max_length=250)
    Item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        related_name='properties_Item',
        verbose_name=_('Item'))

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('Item property')
        verbose_name_plural = _('Item properties')
