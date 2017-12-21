from django import template

from blog.models import Post
from hitcount.models import HitCount

register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular_posts():
    '''
    Тег для шаблона, выводит список популярных
    постов
    '''
    
    #popular = HitCount.objects.filter(content_type='13')[:5]
    popular = Post.objects.all().order_by('-hit_count_generic__hits')[:5]

    context = {
        'popular': popular,
    }

    return context
