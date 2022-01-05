from django.shortcuts import render
from ContactoApp.forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario = FormularioContacto()
    return render(request, 'contacto.html', {'formulario': formulario})
