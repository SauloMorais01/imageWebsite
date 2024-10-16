from django.contrib import admin
from . import models

class AddresInline(admin.StackedInline):
    model = models.Address
    extra = 1

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name']
    inlines= [
        AddresInline
    ]

# Register your models here.
admin.site.register(models.Perfil, PerfilAdmin)
admin.site.register(models.Address)