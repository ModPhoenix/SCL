from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment
from comments.forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/comments_list.html')
def get_comments(instance, object_id, user):
    '''
    Тег для шаблона, выводит список комментариев к объекту
    и форму ввода комментария. Принимает три обярательных
    параметра instance, object_id, user
    '''
    comments = Comment.objects.filter_by_instance(
        instance).order_by('tree_id').select_related()
    comments_count = comments.count()

    content_type = ContentType.objects.get_for_model(instance)

    context = {
        'comments': comments,
        'content_type': content_type,
        'object_id': object_id,
        'user': user,
        'comments_count': comments_count,
    }

    return context


@register.filter
@stringfilter
def upto(value, delimiter=None):
    '''
    {{ date|timesince|upto:',' }}
    '''
    return value.split(delimiter)[0]


upto.is_safe = True
