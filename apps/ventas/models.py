from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellidos