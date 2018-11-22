from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from unidecode import unidecode
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

from blog.utils import get_image, get_excerpt

from taggit.managers import TaggableManager

from hitcount.models import HitCountMixin
from hitcount.models import HitCount

from scl.models import (
    BaseModel,
    ModerationBaseModel,
)


class Guide(ModerationBaseModel, HitCountMixin):
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
        help_text=_('Слаг — это вариант названия, подходящий для URL.'
                    ' Обычно содержит только латинские буквы в нижнем регистре, цифры и дефисы.'))
    content = models.TextField(
        _('Контент'),)
    excerpt = models.TextField(
        _('Описание'),
        blank=True,
        help_text=_('По Умолчанию первый абзац Контента, при необходимости можно изменить.'))
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
    thumbnail_big = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFit(width=540)],
        format='JPEG',
        options={'quality': 95})
    thumbnail_small = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 95})

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('Гайд')
        verbose_name_plural = _('Гайды')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guides:guide_detail", kwargs={"slug": self.slug, "id": self.id})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(unidecode(self.title)[:60])
        if self.thumbnail is None or self.thumbnail == '':
            self.thumbnail = get_image(self.content)
        if self.excerpt == '':
            self.excerpt = strip_tags(get_excerpt(self.content))
        return super(Guide, self).save(*args, **kwargs)

    def get_conttent_type(self):
        conttent_type = ContentType.objects.get_for_model(self.__class__)
        return conttent_type
