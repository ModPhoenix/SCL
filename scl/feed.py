from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from guides.models import Guide

class LatestPostsFeed(Feed):
    title = "Star Citizen Life Посты"
    link = "/"
    description = "Последние опубликованные посты."

    def items(self):
        return Post.objects.filter(published=True, moderation=True)[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return reverse('blog:detail', args=[item.id, item.slug])

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at


class LatestGuidesFeed(Feed):
    title = "Star Citizen Life Гайды"
    link = "/guides/"
    description = "Последние опубликованные гайды."

    def items(self):
        return Guide.objects.filter(published=True, moderation=True)[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return reverse('guides:guide_detail', args=[item.id, item.slug])

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at