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
    telefono = models.CharField('Telefono', max_length=10,null=True)
    tipo_usuario = models.CharField('Tipo de Usuario', choices=TYPE_USER, max_length=1,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManagerVeterinaria()

    USERNAME_FIELD = 'cedula'

    REQUIRED_FIELDS = [
        'correo'
    ]

class Veterinario(User):
    titulo = models.CharField('Titulo',max_length=40)

    class Meta:
        db_table = 'veterinario'
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' - ' +  str(self.cedula)


class Vendedor(User):

    class Meta:
        db_table = 'vendedor'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' - ' +  str(self.cedula)

class Duenio(models.Model):

    GENERO =(
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro'),
    )

    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellidos',max_length=20)
    telefono = models.CharField('Telefono',max_length=12)
    cedula = models.CharField('Cedula',max_length=10, unique=True)
    edad = models.PositiveIntegerField('Edad')
    sexo = models.CharField('Sexo', max_length=1, choices=GENERO)

    class Meta:
        db_table = 'Duenios'
        verbose_name = 'Duenio'
        verbose_name_plural = 'Duenios'


    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' - ' +  str(self.cedula)


class Mascota(models.Model):

    GENERO =(
        ('M','Macho'),
        ('H','Hembra'),
    )

    ESTADO_CHOICES = (
        ('V','Vivo'),
        ('M','Muerto'),
    )

    raza = models.CharField('Raza',max_length=20)
    estado = models.CharField('Estado',max_length=1, choices=ESTADO_CHOICES)
    color = models.CharField('Color',max_length=20)
    especie = models.CharField('Especie',max_length=20)
    edad = models.PositiveIntegerField('Edad')
    nombre = models.CharField('Nombre', max_length=20)
    castrado = models.BooleanField('Castrado',default=False)
    sexo = models.CharField('Sexo', max_length=1, choices=GENERO)
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mascota'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.nombre + ' ' + self.especie