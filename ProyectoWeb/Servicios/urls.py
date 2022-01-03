from django.urls import path
from Servicios.views import servicios

urlpatterns = [
    path('', servicios, name="Servicios"),
]
