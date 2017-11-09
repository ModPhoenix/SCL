from django import template
from django.template.defaultfilters import stringfilter

from mttp_comments.models import Comment

register = template.Library()

@register.inclusion_tag('mttp_comments/mttp_comments.html')
def get_comments(obj):

    comments = Comment.objects.filter_by_instance(obj).order_by('tree_id').select_related()

    return {'comments': comments}

@register.filter
@stringfilter
def upto(value, delimiter=None):
    ''' 
    {{ date|timesince|upto:',' }}
    '''
    return value.split(delimiter)[0]

upto.is_safe = True
