from django.urls import path
from TiendaApp.views import tienda


urlpatterns = [
    path('', tienda, name="Tienda"),
]