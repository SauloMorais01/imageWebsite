from django.contrib import admin
from . import models

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 1

class RequestAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

# Register your models here.
admin.site.register(models.Request, RequestAdmin)
admin.site.register(models.OrderItem)