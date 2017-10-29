from django.contrib import admin
#from simple_history.admin import SimpleHistoryAdmin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from .models import Funding, Ship, Company

@admin.register(Ship)
class ShipAdmin(CompareVersionAdmin):
    list_display = ('id', 'name', 'manufacturer', 'focus', 'max_crew',)
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