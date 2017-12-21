from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from unidecode import unidecode
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.contrib.sitemaps import Sitemap

from hitcount.models import HitCountMixin
from hitcount.models import HitCount

from .utils import get_image, get_excerpt

from scl.models import (
    BaseModel,
    ModerationBaseModel,
)


class Category(MPTTModel, BaseModel):
    """
    Модель категорий для постов 
    """
    name = models.CharField(
        _("Название"),
        max_length=250,
        help_text=_('Название определяет, как катерогия будет отображаться на сайте.'))
    slug = models.SlugField(
        _("Слаг"),
        help_text=_('Слаг — это вариант названия, подходящий для URL. Обычно содержит только латинские буквы в нижнем регистре, цифры и дефисы.'))
    description = models.TextField(
        _("Описание"),
        blank=True,
        help_text=_('Описание - будет выводится в мета теге description.'))
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Родительская'),
        help_text=_('Категории, в отличие от меток, могут иметь иерархию.'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    class MPTTMeta:
        order_insertion_by = ['name']


class Post(ModerationBaseModel, HitCountMixin):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Автор'))
    title = models.CharField(
        _('Заголовок'),
        max_length=150)
    slug = models.SlugField(
        _('Слаг'),
        max_length=60,
        unique=False,
        help_text=_('Слаг — это вариант названия, подходящий для URL. Обычно содержит только латинские буквы в нижнем регистре, цифры и дефисы.'))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Катерогия"))
    content = models.TextField(
        _('Контент'),)
    excerpt = models.TextField(
        _('Описание'),
        blank=True,
        help_text=_('По Умолчанию первый абзац Контента, при необходимости можно изменить.'))
    main = models.BooleanField(
        _('Главная страница'),
        default=False,
        help_text=_('Решает будет ли запись видна на главной странице.'))
    ordering = models.SmallIntegerField(
        _('Сортировка'),
        default=0,
        blank=True,
        null=True)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    thumbnail = models.ImageField(
        _('Миниатюра'),
        blank=True,
        null=True)
    big_thumbnail = models.BooleanField(
        _('Большая миниатюра'),
        default=False,
        help_text=_('Если отмечено, на превью будет большая миниатюра.'))
    thumbnail_540 = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFit(width=540)],
        format='JPEG',
        options={'quality': 95})
    thumbnail_100 = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 95})

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug, "id": self.id})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(unidecode(self.title)[:60])
        if self.thumbnail == None or self.thumbnail == '':
            self.thumbnail = get_image(self.content)
        if self.excerpt == '':
            self.excerpt = strip_tags(get_excerpt(self.content))

        return super(Post, self).save(*args, **kwargs)

    def get_conttent_type(self):
        conttent_type = ContentType.objects.get_for_model(self.__class__)
        return conttent_type


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Post.objects.filter(published=True, moderation=False)

    def lastmod(self, obj):
        return obj.created_at
