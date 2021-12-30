from django.core.exceptions import AppRegistryNotReady
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return 'El cliente se llama %s %s, su direccion física es %s y la de correo es %s. Su contacto es %s' % (self.nombre, self.apellido, self.direccion, self.email, self.telefono)



class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre %s, la sección es %s y el precio es %s' % (self.nombre,self.seccion, str(self.precio))
            


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        if self.entregado:
            return 'El pedido %s fue de %s y su estado es entregado' % (self.numero, self.fecha)
        else:
            return 'El pedido %s fue de %s y su estado es no entregado' % (self.numero, self.fecha)