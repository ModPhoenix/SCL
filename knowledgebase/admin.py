from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from .models import (
    Page,
    Funding,
    Ship,
    Company,
)


@admin.register(Page)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'published')
    list_display_links = ('title',)


@admin.register(Ship)
class ShipAdmin(CompareVersionAdmin):
    list_display = ('id', 'name', 'manufacturer', 'max_crew',)
    list_display_links = ('name',)


@admin.register(Company)
class CompanyAdmin(CompareVersionAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class FundingAdmin(admin.ModelAdmin):
    list_display = ('id', 'funds', 'fans', 'date',)
    list_display_links = ('funds',)


admin.site.register(Funding, FundingAdmin)
