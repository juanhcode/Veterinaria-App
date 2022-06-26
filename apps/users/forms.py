from django import forms
from django.contrib.auth import authenticate
from .models import Administrador, Vendedor, Veterinario

from django.forms import DateInput, EmailInput, NumberInput, TextInput


class UserRegisterFormAdministrador(forms.ModelForm):

    #Aqui es donde se piden las contrasenias de forma mas segura
    password1 = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Repetir Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )


    class Meta:
        model = Administrador
        #Jamas se guarda una contrasenia como dato plano, es por ello que no lo pedimos en los fields

        fields = (
            'nombre',
            'apellidos',
            'cedula',
            'edad',
            'sexo',
            'correo',
            'telefono',
            'fecha_ingreso',
            
        )
        widgets = {
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'cedula': forms.NumberInput(),
            'edad': forms.NumberInput(),
            'sexo': forms.Select(),
            'correo': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'fecha_ingreso': forms.DateInput(),
        }

class UserRegisterFormVendedor(forms.ModelForm):

    #Aqui es donde se piden las contrasenias de forma mas segura
    password1 = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Constraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Constraseña'
            }
        )
    )


    class Meta:
        model = Vendedor
        #Jamas se guarda una contrasenia como dato plano, es por ello que no lo pedimos en los fields

        fields = (
            'nombre',
            'apellidos',
            'cedula',
            'edad',
            'sexo',
            'correo',
            'telefono',
            'fecha_ingreso',
            
        )
        widgets = {
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'cedula': forms.NumberInput(),
            'edad': forms.NumberInput(),
            'sexo': forms.Select(),
            'correo': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'fecha_ingreso': forms.DateInput(),
        }

    

    #validacion si la contrasenia 2 es diferente a la 1
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contrasenias no son iguales')
        #Verificando que la contrasenia tenga mas de 5 caracteres    
        elif len(self.cleaned_data['password1']) < 5:
            self.add_error('password1','Las contrasenias deben tener mas de 5 digitos')


class UserRegisterFormVeterinario(forms.ModelForm):

    #Aqui es donde se piden las contrasenias de forma mas segura
    password1 = forms.CharField(
        label = 'Contrasenia',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Constraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Constraseña'
            }
        )
    )

    class Meta:
        model = Veterinario
        #Jamas se guarda una contrasenia como dato plano, es por ello que no lo pedimos en los fields

        fields = (
            'nombre',
            'apellidos',
            'cedula',
            'edad',
            'sexo',
            'correo',
            'telefono',
            'fecha_ingreso',
            'titulo'
            
        )
        widgets = {
            'nombre': TextInput(),
            'apellidos': TextInput(),
            
            'edad': NumberInput(),
            'sexo': forms.Select(),
            'correo': EmailInput(),
            'telefono': NumberInput(),
            'fecha_ingreso': DateInput(),
            'titulo': TextInput(),
        }

    

    #validacion si la contrasenia 2 es diferente a la 1
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contrasenias no son iguales')
        #Verificando que la contrasenia tenga mas de 5 caracteres    
        elif len(self.cleaned_data['password1']) < 5:
            self.add_error('password1','Las contrasenias deben tener mas de 5 digitos')






#heredamos del Form normal ya que no dependemos de ningun modelo
class LoginForm(forms.Form):

    cedula = forms.CharField(
        label = 'cedula',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'cedula'
            }
        )
    )

    password = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':' Constraseña'
            }
        )
    )
        

    def clean(self):
        cleaner_data = super(LoginForm, self).clean
        cedula = self.cleaned_data['cedula']
        password = self.cleaned_data['password']

        if not authenticate(cedula = cedula, password= password):
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return self.cleaned_data


#Form de agregar una vista