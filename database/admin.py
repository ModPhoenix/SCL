from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from .models import (
    Category,
    Funding,
    Ship,
    Company,
)


@admin.register(Ship)
class ShipAdmin(CompareVersionAdmin):
    list_display = ('id', 'name', 'manufacturer', 'max_crew',)
    list_display_links = ('name',)

# admin.site.register(Ship, ShipAdmin)


@admin.register(Company)
class CompanyAdmin(CompareVersionAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

# admin.site.register(Company, CompanyAdmin)


class FundingAdmin(admin.ModelAdmin):
    list_display = ('id', 'funds', 'fans', 'date',)
    list_display_links = ('funds',)


admin.site.register(Funding, FundingAdmin)
