from django.shortcuts import render, redirect

from CarritoApp.carrito import Carrito
from TiendaApp.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.agregar(producto)

    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.eliminar(producto)

    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.restar(producto)

    return redirect("Tienda")

def limpiar_carro(request):
    carrito = Carrito(request)

    carrito.limpiar()

    return redirect("Tienda")