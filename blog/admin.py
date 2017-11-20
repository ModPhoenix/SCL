from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Post

@admin.register(Post)
class PostAdmin(CompareVersionAdmin):
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('title',)