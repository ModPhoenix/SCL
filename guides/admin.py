from django.contrib import admin

from .models import Guide

@admin.register(Guide)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'published', 'moderation',)
    list_display_links = ('title',)
