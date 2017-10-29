from django.db import models
from django.utils import timezone
from django.utils.translation import to_locale, get_language, ugettext_lazy as _


class BaseModel(models.Model):
    """
    Absrtact model
    Add to standart models date of
    crete and update
    """
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_(u'Дата создания'))
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_(u'Дата изменения'))

    objects = models.Manager()

    class Meta:
        abstract = True

    def update(self):
        self.updated_at = timezone.now()
        self.save()

class ModerationBaseModel(BaseModel):
    """
    Absrtact model
    Add to BaseModel  published,
    moderation
    """
    published = models.BooleanField(
        _(u'Опубликовано'),
        default=True,
        help_text=_('Решает будет ли запись видна на сайте.'))
    
    moderation = models.BooleanField(
        _(u'Модерация'),
        default=False,
        help_text=_('Если отмечено, запись заблокирована модератором.'))

    class Meta:
        abstract = True
