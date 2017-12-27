from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.utils.translation import to_locale, get_language, ugettext_lazy as _


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<id>/<filename>
    return 'avatars/{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    ''' 
    Расширенная модель пользователя
    Добавляет к стандартной поля
    avatar, birthdate, biography,
    location, organization,
    handle
    '''
    avatar = ProcessedImageField(
        upload_to=user_directory_path,
        default = 'avatars/1.jpg',
        blank=True,
        null=True,
        processors=[ResizeToFill(290, 290)],
        format='JPEG',
        options={'quality': 95},
        verbose_name=_(u'Аватар пользователя'))
    
    avatar_thumbnail_40 = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(40, 40)],
        format='JPEG',
        options={'quality': 95},)

    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name=_(u'День рождения'))
    biography = models.TextField(
        blank=True,
        verbose_name=_(u'О себе'))
    location = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_(u'Локация'))
    organization = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_(u'Игровая Организация'))
    handle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_(u'UEE Handle'))
