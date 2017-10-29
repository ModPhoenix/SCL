from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.encoding import force_text
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from unidecode import unidecode
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from .utils import get_image

from scl.models import (
    BaseModel,
    ModerationBaseModel,
    )

class Post(ModerationBaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    title = models.CharField(
        max_length=150)
    slug = models.SlugField(
        max_length=60,
        unique=False)
    content = models.TextField()
    excerpt = models.TextField(
        blank=True)
    thumbnail = models.ImageField(
        blank=True,
        null=True)
    thumbnail_540 = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFit(width=540)],
        format='JPEG',
        options={'quality': 95})

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug, "id": self.id})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(unidecode(self.title)[:60])
        if self.thumbnail == '':
            self.thumbnail = get_image(self.content)
        if self.excerpt == '':
            self.excerpt = strip_tags(self.content)[:100] + '...'
        return super(Post, self).save(*args, **kwargs)

    def get_conttent_type(self):
        conttent_type = ContentType.objects.get_for_model(self.__class__)
        return conttent_type
