from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

COMMENT_MAX_LENGTH = getattr(settings, 'COMMENT_MAX_LENGTH', 3000)


class CommentManager(models.Manager):

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        qs = super(CommentManager, self).filter(
            content_type=content_type, object_id=object_id)
        return qs


class CommentAbstractModel(MPTTModel):
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name="content_type_set_for_%(class)s",
        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class Comment(CommentAbstractModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name="%(class)s_comments",
        on_delete=models.CASCADE)
    comment = models.TextField(
        _('comment'),
        max_length=COMMENT_MAX_LENGTH)
    karma = models.SmallIntegerField(
        default=0)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name=_('children'),
        db_index=True,
        on_delete=models.CASCADE)
    is_public = models.BooleanField(
        _('Публичный'),
        default=True,
        help_text=_('Если отмечено комментарий виден на сайте.'))
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_(u'Дата Создания'))
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_(u'Дата Редактирования'))

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    objects = CommentManager()

    class Meta(CommentAbstractModel.Meta):
        ordering = ['-created_at']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return "%s: %s..." % (self.user.username, self.comment[:50])
