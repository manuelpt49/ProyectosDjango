from django.shortcuts import render
from BlogApp.models import Categoria, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    unique_categorias = obtaining_categories(posts)
    return render(request, "blog.html", {'posts': posts, 'categorias': unique_categorias})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    return render(request, "categoria.html", {'categoria': categoria, 'posts':posts})


def obtaining_categories(posts):
    """Class to obtain categories according to posts available in webpage"""
    unique_categorias = []
    for post in posts:
        for categoria in post.categorias.all():
            #unique_categorias.append({categoria.nombre, categoria.id})
            unique_categorias.append(categoria)
    unique_categorias = set(unique_categorias)
    return unique_categorias
