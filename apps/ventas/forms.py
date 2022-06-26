from dataclasses import fields
from email.headerregistry import Group
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import Textarea, TextInput, NumberInput

from .models import Factura, Producto


class ProductoRegisterForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('identificacion','nombre', 'descripcion', 'precio', 'iva', 'stock', 'vendedor')
        widgets = {
            'identificacion':NumberInput(),
            'nombre': TextInput(),
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 2, 'style':'resize:none;', 'id':'descripcionInput'}),
            'precio': NumberInput(),
            'iva': NumberInput(),
            'stock': NumberInput(),
            'vendedor': forms.Select()
        }


