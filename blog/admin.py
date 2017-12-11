from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_display_links = ('name',)

@admin.register(Post)
class PostAdmin(CompareVersionAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at', 'published', 'moderation',)
    list_display_links = ('title',)