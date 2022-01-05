from django.urls import path
from ContactoApp.views import contacto

urlpatterns = [
    path('', contacto, name="Contacto"),
]