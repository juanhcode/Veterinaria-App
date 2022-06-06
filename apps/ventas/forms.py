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
        fields = ('identificacion','nombre', 'descripcion', 'precio', 'iva', 'stock', 'vendedor')
        widgets = {
            'identificacion':NumberInput(),
            'name': TextInput(),
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 2, 'style':'resize:none;', 'id':'descripcionInput'}),
            'precio': NumberInput(),
            'iva': NumberInput(),
            'stock': NumberInput(),
            'vendedor': forms.Select()
        }


