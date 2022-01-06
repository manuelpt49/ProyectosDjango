from django.contrib import admin

# Register your models here.

from TiendaApp.models import CategoriaProd, Producto

class CategoriaProdAdmin (admin.ModelAdmin):
    #readonly_fields = ('created', 'updated') #Fields showed in panel
    list_display = ("nombre", "created", "updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)

class ProductoAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Fields showed in panel
    list_display = ("nombre", "precio", "created", "updated")

admin.site.register(Producto, ProductoAdmin)