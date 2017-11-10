from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment
from comments.forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/comments_list.html')
def get_comments(instance):

    comments = Comment.objects.filter_by_instance(
        instance).order_by('tree_id').select_related()

    return {'comments': comments}

@register.inclusion_tag('comments/comment_form.html')
def get_comment_form(instance, object_id):

    content_type = ContentType.objects.get_for_model(instance)
    print('content_type:', content_type)

    return {'content_type': content_type, 'object_id': object_id}


@register.filter
@stringfilter
def upto(value, delimiter=None):
    '''
    {{ date|timesince|upto:',' }}
    '''
    return value.split(delimiter)[0]


upto.is_safe = True
