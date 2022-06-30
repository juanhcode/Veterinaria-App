from cProfile import label
from pyexpat import model
from django.db import models

# Create your models here.

class PruebaModelo(models.Model):
    mensaje = models.CharField("Mensaje", max_length=20, default='Hola Mundo')

    class Meta:
        db_table = 'prueba'
        verbose_name = 'PruebaModelo'
        verbose_name_plural = 'PruebaModelos'

    def __str__(self):
        return self.mensaje