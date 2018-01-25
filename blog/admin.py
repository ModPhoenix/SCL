from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Post

from .forms import PostAdminForm


@admin.register(Post)
class PostAdmin(CompareVersionAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'ordering', 'created_at', 'updated_at', 'published', 'moderation',)
    list_display_links = ('title',)