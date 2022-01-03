from django.contrib import admin

# Register your models here.

from Servicios.models import Servicio

class ServicioAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Fields showed in panel
    list_display = ("titulo", "contenido", "imagen", "created", "updated")

admin.site.register(Servicio, ServicioAdmin)