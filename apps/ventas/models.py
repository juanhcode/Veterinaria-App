from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.CharField('Descripcion', max_length=50, null=True)
    precio = models.PositiveIntegerField(default=0)
    iva = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
   
    def __str__(self):
        return self.nombre 
