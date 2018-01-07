from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post
from guides.models import Guide
from taggit.models import Tag

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'

    def items(self):
        return Post.objects.filter(published=True, moderation=True)

    def lastmod(self, obj):
        return obj.created_at


class GuideSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'

    def items(self):
        return Guide.objects.filter(published=True, moderation=True)

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.2
    protocol = 'https'

    def items(self):
        return ['about', 'careers', 'terms', 'privacy']

    def location(self, item):
        return reverse(item)