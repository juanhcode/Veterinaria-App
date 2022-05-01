from django.db import models

# Create your models here.
<<<<<<< HEAD

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellidos
=======
>>>>>>> 3618d22738bd3e12c85848d3bd5fe5a409ec2566
