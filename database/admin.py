from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from .models import (
    Funding,
    Ship,
    Company,
    Category,
    Item,
    CategoryProperty,
    ItemProperty,
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

''' 
/////////////////////////////////////////////////////////////////////////////////////////////
'''

class ItemPropertyInline(admin.TabularInline):
    model = ItemProperty
    extra = 1
    verbose_name_plural = 'Values'
    suit_classes = 'suit-tab suit-tab-values'

@admin.register(CategoryProperty)
class CategoryPropertyAdmin(admin.ModelAdmin):
    inlines = [ItemPropertyInline,]
    suit_form_tabs = (('general', 'General'), 
        ('values', 'Values'), )
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
             'name',
             'category',
             'published',
             ]
        }),
    ]

@admin.register(ItemProperty)
class ItemPropertyAdmin(admin.ModelAdmin):
    pass

class CategoryPropertyInline(admin.TabularInline):
    model = CategoryProperty
    extra = 1
    verbose_name_plural = 'Params'
    suit_classes = 'suit-tab suit-tab-params'

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    
    inlines = [CategoryPropertyInline,]
    suit_form_tabs = (('general', 'General'), 
        ('params', 'Params'), 
        ('filters','Filters'))
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
             'name',
             'slug',
             'title',
             'description',
             'keywords',
             'image',
             'parent',
             'url',
             ]
        }),
    ]
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }

@admin.register(Item)
class ItemAdmin( admin.ModelAdmin):
    inlines = [ItemPropertyInline,]
    list_display = ('name', 'category', 'published')
    list_filter = ('category',)
    serch_fields = ['id','name']
    suit_form_tabs = (('general', 'General'), 
        ('offers', 'Offers'),
        ('params', 'Params'), 
        ('filters','Filters'),
        ('images','Images'),)
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name',
             'slug',
             'title',
             'description',
             'keywords',
             'image',
             'category',
             'url',
             'price',]
        }),
    ]
    
    
    
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }


