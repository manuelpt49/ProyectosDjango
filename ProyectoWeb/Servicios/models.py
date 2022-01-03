from django.db import models

# Create your models here.
class Servicio (models.Model):
    titulo = models.CharField(max_length=15)
    contenido = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True)

    class Meta: #Class to define how Servicio class will call inside django panel
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo
