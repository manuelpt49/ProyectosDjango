from django.urls import path
from CarritoApp.views import agregar_producto, eliminar_producto, limpiar_carro, restar_producto

app_name = "carrito"

urlpatterns = [
    path('agregar/<int:producto_id>/', agregar_producto, name="Agregar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Eliminar"),
    path('restar/<int:producto_id>/', restar_producto, name="Restar"),
    path('limpiar/', limpiar_carro, name="Limpiar"),
]