from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.translation import to_locale, get_language, ugettext_lazy as _


class User(AbstractUser):
    ''' 
    Расширенная модель пользователя
    Добавляет к стандартной поля
    avatar, birthdate, biography,
    location, organization,
    handle
    '''
    avatar = ProcessedImageField(
        upload_to='avatars',
        default = 'avatars/1.jpg',
        blank=True,
        null=True,
        processors=[ResizeToFill(255, 255)],
        format='JPEG',
        options={'quality': 99},
        verbose_name=_(u'Аватар пользователя'))
    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name=_(u'День рождения'))
    biography = models.TextField(
        blank=True,
        verbose_name=_(u'О себе'))
    location = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_(u'Локация'))
    organization = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_(u'Игровая Организация'))
    handle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_(u'UEE Handle'))
