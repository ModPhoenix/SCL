from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(CompareVersionAdmin):
    list_display = ('title', 'author', 'tags', 'ordering', 'created_at', 'updated_at', 'published', 'moderation',)
    list_display_links = ('title',)