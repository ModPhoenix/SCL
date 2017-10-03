from django.contrib import admin

from .models import Funding, Ship, Company

class ShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'focus', 'max_crew',)
    list_display_links = ('name',)

admin.site.register(Ship, ShipAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

admin.site.register(Company, CompanyAdmin)

class FundingAdmin(admin.ModelAdmin):
    list_display = ('id', 'funds', 'fans', 'date',)
    list_display_links = ('funds',)

admin.site.register(Funding, FundingAdmin)