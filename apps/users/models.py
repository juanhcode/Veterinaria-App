from pyexpat import model
from django.db import models

from .managers import UserManagerVeterinaria

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    TYPE_USER =(
        ('1','Veterinario'),
        ('2','Vendedor'),
        ('3','Administrador'),
    )

    GENERO =(
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro'),
    )
    
    nombre = models.CharField('Nombre', max_length=20,null=True)
    apellidos = models.CharField('Apellidos', max_length=50,null=True)
    cedula = models.CharField('Cedula', max_length=12, unique=True)
    fecha_ingreso = models.DateField('Fecha de Ingreso', null=True)
    edad = models.PositiveIntegerField('Edad',null=True)
    sexo = models.CharField('Sexo', choices=GENERO,max_length=1,null=True)
    correo = models.EmailField('Correo Electronico',null=True)
    telofono = models.CharField('Telofono', max_length=10,null=True)
    tipo_usuario = models.CharField('Tipo de Usuario', choices=TYPE_USER, max_length=1,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManagerVeterinaria()

    USERNAME_FIELD = 'cedula'

    REQUIRED_FIELDS = [
        'correo'
    ]
   

    def get_full_name(self):
        return self.nombre + ' ' + self.apellidos
    

class Veterinario(User):
    titulo = models.CharField('Titulo',max_length=40)

    class Meta:
        db_table = 'veterinario'
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'


class Vendedor(User):

    class Meta:
        db_table = 'vendedor'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

