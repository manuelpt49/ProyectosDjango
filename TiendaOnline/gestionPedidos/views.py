from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    data = request.GET['producto']
    #mensaje = "Buscando... %r" %request.GET['producto']
    articulos = Articulos.objects.filter(nombre__icontains = data)
    return render(request, "resultados_busqueda.html", {'articulos': articulos, 'query': data})
