from django.db import models

from apps.users.models import Vendedor, Duenio

# Create your models here.

class Producto(models.Model):
    identificacion = models.PositiveBigIntegerField('Codigo', unique=True, default=0)
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField(null=True)
    precio = models.PositiveIntegerField(default=0)
    iva = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
   
    def __str__(self):
        return  str(self.id) + ' ' +self.nombre 


class Factura(models.Model):

    fecha = models.DateField('Fecha', auto_now_add=True)
    total = models.PositiveIntegerField('Total factura')
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return  str(self.fecha) + ' / ' + str(self.id)


   
