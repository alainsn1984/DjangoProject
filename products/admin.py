from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product
# Register your models here.

def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e' )
# Action description

change_rating.short_description = "Mark Selected Products as Excellent"

class ProductA(admin.ModelAdmin):
    # exclude= ('description',)
    list_display = ('name', 'description', 'mfg_date', 'rating',)
    list_filter = ('mfg_date',)
    actions = [change_rating]

admin.site.site_header = 'Demo Project'
admin.site.register(Product, ProductA)
admin.site.unregister(Group)

