from django import template

from guides.models import Guide
from hitcount.models import HitCount

register = template.Library()


@register.inclusion_tag('guides/popular_guides.html')
def get_popular_guides():
    '''
    Тег для шаблона, выводит список популярных
    гайдов
    '''
    
    popular_guides = Guide.objects.all().order_by('-hit_count_generic__hits')[:5]

    context = {
        'popular_guides': popular_guides,
    }

    return context
