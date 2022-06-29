from django.db import models
from django.urls import reverse

from apps.users.models import Vendedor, Duenio

from .managers import VentasManager

# Create your models here.

class Producto(models.Model):
    identificacion = models.PositiveBigIntegerField('Codigo', unique=True, default=0)
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField(null=True)
    precio = models.PositiveIntegerField(default=0)
    iva = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    objects = VentasManager()

    class Meta:
        ordering = ['id','nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
   
    def __str__(self):
        return  str(self.id) + ' ' +self.nombre 

    def get_pk(self):
        return reverse('ventas_app:agregarcarro',
            kwargs={'pk':self.id}
        ) 


class Factura(models.Model):
    numero_factura = models.PositiveBigIntegerField('Numero Factura', unique=True, default=0)
    fecha = models.DateField('Fecha', auto_now_add=True)
    total = models.PositiveIntegerField('Total factura')
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return  str(self.fecha) + ' / ' + str(self.id)


class Carro(models.Model):
    cliente = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField('Fecha', auto_now_add=True)

    def __str__(self):
        return "Carro: " + str(self.id) + ' - ' + "Fecha:" + str(self.created_at)


class ProductoCarro(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,  null=True, blank=True)
    rate = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Carro: " + str(self.carro.id) + "Producto en carro" + str(self.id)


class Pedido(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)
    pedido_por = models.CharField(max_length=200)
    subtotal = models.PositiveIntegerField()
    descuento = models.PositiveIntegerField()
    total = models.PositiveIntegerField(null=True, blank=True)
    creado_el = models.DateField(auto_now_add=True)

    objects = VentasManager()

    def __str__(self):
        return "Pedido: " + str(self.id) + ' - ' + 'Fecha: ' + str(self.creado_el) 

    
    


   
