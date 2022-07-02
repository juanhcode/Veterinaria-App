from tkinter import Widget
from django import forms
from django.forms import Textarea, TextInput, NumberInput

from .models import Producto, Pedido


class ProductoRegisterForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('identificacion','nombre', 'descripcion', 'precio', 'iva', 'stock', 'vendedor')
        widgets = {
            'identificacion':forms.NumberInput(),
            'nombre': forms.TextInput(),
            'descripcion': forms.Textarea(attrs={'cols': 20, 'rows': 2, 'style':'resize:none;', 'id':'descripcionInput'}),
            'precio': forms.NumberInput(),
            'iva': forms.NumberInput(),
            'stock': forms.NumberInput(),
            'vendedor': forms.Select()
        }

    def clean(self):
        cleaned_data = super(ProductoRegisterForm, self).clean
        identificacion = self.cleaned_data['identificacion']
        
        if Producto.objects.filter(identificacion=identificacion).exists():
            print('entre en el if vendedor')
            raise forms.ValidationError("Este id ya a sido registrado")
        
        return self.cleaned_data

        


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = (
            'identificacion_factura',
            'pedido_por',
            'cedula',
            'telefono',
            'direccion'
        )
        widgets = {
            'identificacion_factura':forms.TextInput(),
            'pedido_por': forms.TextInput(),
            'cedula': forms.NumberInput(),
            'telefono': forms.NumberInput(),
            'direccion': forms.TextInput(),
        }