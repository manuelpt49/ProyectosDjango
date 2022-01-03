from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre


class Post (models.Model):
    titulo = models.CharField(max_length=25)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="blog", null = True, blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.titulo