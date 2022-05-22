from email.headerregistry import Group
from django import forms
from django.forms import Textarea, TextInput, NumberInput

from apps.users.models import Vendedor
from .models import Producto


class ProductoRegisterForm(forms.ModelForm):
    '''
    def __init__(self, *args, **kwargs):
        self.fields['vendedor'].queryset = Vendedor.objects.all()'''

    #vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.all())

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'iva', 'stock', 'vendedor')
        widgets = {
            'name': TextInput(),
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 2, 'style':'resize:none;', 'id':'descripcionInput'}),
            'precio': NumberInput(),
            'iva': NumberInput(),
            'stock': NumberInput(),
            'vendedor': forms.Select()
        }


    '''
    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    descripcion = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'form-control'
            }
        )
    )

    precio = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    iva = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    stock = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )'''

