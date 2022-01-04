from django.shortcuts import render
from BlogApp.models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    unique_categorias = []
    for post in posts:
        for categoria in post.categorias.all():
            unique_categorias.append(categoria.nombre)
    unique_categorias = set(unique_categorias)
    return render(request, "blog.html", {'posts': posts, 'categorias': unique_categorias})