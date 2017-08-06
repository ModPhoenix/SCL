from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        qs = super(CommentManager, self).filter(
            content_type=content_type, object_id=object_id).filter(parent=None)
        return qs


class CommentAbstractModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class Comment(CommentAbstractModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(unique=False)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    karma = models.IntegerField(default=0)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)

    objects = CommentManager()

    class Meta(CommentAbstractModel.Meta):
        ordering = ['date']

    def __str__(self):
        return "%s: %s..." % (self.author.username, self.content[:50])

    def children(self):
        return Comment.objects.filter(parent=self)
