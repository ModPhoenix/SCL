from django.contrib import admin

from .models import Funding
    
class FundingAdmin(admin.ModelAdmin):
    list_display = ('id', 'funds', 'fans', 'date',)
    list_display_links = ('funds',)

admin.site.register(Funding, FundingAdmin)