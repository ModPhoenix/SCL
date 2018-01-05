from django.contrib import admin

from .models import Guide

from .forms import GuideAdminForm

@admin.register(Guide)
class CategoryAdmin(admin.ModelAdmin):
    form = GuideAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at', 'published', 'moderation',)
    list_display_links = ('title',)
