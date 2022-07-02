from dataclasses import field
from email.headerregistry import Group
from tkinter import Widget
from django import forms
from django.forms import Textarea, TextInput, NumberInput

from apps.users.models import  Duenio, Mascota
from apps.veterinario.models import HistorialClinico


class ResponsableRegisterForm(forms.ModelForm):

    class Meta:
        model = Duenio
        fields = ('__all__')
        widgets = {
            'cedula':forms.NumberInput(),
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'telefono': forms.NumberInput(),
            'edad': forms.NumberInput(),
            'sexo': forms.Select(),
            'direccion': forms.TextInput()
        } 

    def clean(self):
        cleaned_data = super(ResponsableRegisterForm, self).clean
        cedula = self.cleaned_data['cedula']
        telefono = self.cleaned_data['telefono']

        if len(cedula) > 10:
            print('Entre en el if')
            raise forms.ValidationError('El campo de cedula solo permite hasta 10 numeros')

        elif len(telefono) > 10:
            raise forms.ValidationError('El campo de telefono solo permite hasta 10 numeros')

        elif Duenio.objects.filter(cedula=cedula).exists():
            print('entre en el if vendedor')
            raise forms.ValidationError("Esta cedula ya a sido registrada")
        
        elif Duenio.objects.filter(telefono=telefono).exists():
            print('entre en el if vendedor')
            raise forms.ValidationError("Este telefono ya a sido registrado")
        
        return self.cleaned_data


class MascotaRegisterForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ('__all__')
        widgets = {
            'raza':forms.TextInput(),
            'estado': forms.Select(),
            'color': forms.TextInput(),
            'especie': forms.TextInput(),
            'edad': forms.NumberInput(),
            'nombre': forms.TextInput(),
            'castrado': forms.NullBooleanSelect(),
            'sexo': forms.Select(),
            'duenio': forms.Select(),
        }

class HistorialRegisterForm(forms.ModelForm):

    class Meta:
        model = HistorialClinico
        fields = ('__all__')
        widgets = {
            'anamnesis': forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'anamnesisInput'},),
            'patologia': forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'patologiaInput'},),
            'peso': forms.NumberInput(),
            'examen_fisico': forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'examen_fisicoInput'},),
            'frecuencia_cardiaca': forms.NumberInput(),
            'diagnostico': forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'diagnosticoInput'},),
            'vacunas': forms.TextInput(),
            'tratamiento': forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'tratamientoInput'},),
            'temperatura': forms.NumberInput(),
            'detalles_visita':forms.Textarea(attrs={'cols': 100, 'rows': 4, 'style':'resize:none;', 'id':'tratamientoInput'},),
            'veterinario': forms.Select(),
            'mascota': forms.Select(),
        }

