from django.contrib import admin

# Register your models here.

from Servicios.models import Servicio

class ServicioAdmin (admin.ModelAdmin):
    list_display = ("titulo", "contenido", "created", "updated")

admin.site.register(Servicio, ServicioAdmin)