from django.shortcuts import render
from TiendaApp.models import Producto, CategoriaProd

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    categorias = obtaining_categories(productos)
    return render(request, "tienda.html", {'productos': productos, 'categorias':categorias})

def obtaining_categories(productos):
    """Class to obtain categories according to posts available in webpage"""
    unique_categorias = []
    for producto in productos:
        for categoria in producto.categorias.all():
            #unique_categorias.append({categoria.nombre, categoria.id})
            unique_categorias.append(categoria)
    unique_categorias = set(unique_categorias)
    return unique_categorias