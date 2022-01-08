from django.db import models

# Create your models here.

class CategoriaProd (models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Producto (models.Model):
    nombre = models.CharField(max_length=15)
    categorias = models.ManyToManyField(CategoriaProd)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="tienda", null = True, blank = True)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("{} ${}, Stock: {}, Categorias: {}".format(self.nombre, self.precio, self.stock, self.categorias))
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"