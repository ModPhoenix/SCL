from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from .models import Post

admin.site.register(Post, CompareVersionAdmin)