from django.contrib import admin
from . import models

class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'shot_description', 'get_price_formater', 'get_promotinal_price_formater', 'type', 'stockPerPurchase']
    inlines = [
        VariationInline
    ]

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
