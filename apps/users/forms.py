from django import forms
from django.contrib.auth import authenticate
from .models import Administrador, User, Vendedor, Veterinario

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

    cedula = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Digite su cedula'
            }
        )
    )

    telefono = forms.CharField(
        required=True,
        widget=forms.NumberInput(
        )
    )
        
    class Meta:
        model = Administrador
        #Jamas se guarda una contrasenia como dato plano, es por ello que no lo pedimos en los fields

        fields = (
            'cedula',
            'nombre',
            'apellidos',
            'edad',
            'sexo',
            'correo',
            'telefono',
            'fecha_ingreso',
            
        )
        widgets = {
            'cedula': forms.NumberInput(),
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'edad': forms.NumberInput(),
            'sexo': forms.Select(),
            'correo': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'fecha_ingreso': forms.DateInput(),
        }

    def clean(self):
        cleaned_data = super(UserRegisterFormAdministrador, self).clean
        cedula = self.cleaned_data['cedula']
        telefono = self.cleaned_data['telefono']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        correo = self.cleaned_data['correo']

        if password1 != password2:
            raise forms.ValidationError('Las contrasenias no son iguales')

        #Verificando que la contrasenia tenga mas de 5 caracteres    
        elif len(password1) < 5:
            raise forms.ValidationError('Las contrasenias deben tener mas de 5 digitos')

        elif len(cedula) > 10:
            print('Entre en el if')
            raise forms.ValidationError('El campo de cedula solo permite hasta 10 numeros')

        elif len(telefono) > 10:
            raise forms.ValidationError('El campo de telefono solo permite hasta 10 numeros')

        elif User.objects.filter(cedula=cedula).exists():
            print('entre en el if vendedor')
            raise forms.ValidationError("Esta cedula ya a sido registrada")
        
        elif User.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya a sido registrado")
            
        elif User.objects.filter(telefono=telefono).exists():
            raise forms.ValidationError("Este telefono ya a sido registrado")
        
        return self.cleaned_data


    
class UserRegisterFormVendedor(forms.ModelForm):

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
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    cedula = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Digite su cedula'
            }
        )
    )

    telefono = forms.CharField(
        required=True,
        widget=forms.NumberInput(
        )
    )
       

    def clean(self):
        cleaned_data = super(UserRegisterFormVendedor, self).clean
        cedula = self.cleaned_data['cedula']
        telefono = self.cleaned_data['telefono']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        correo = self.cleaned_data['correo']

        if password1 != password2:
            raise forms.ValidationError('Las contrasenias no son iguales')

        #Verificando que la contrasenia tenga mas de 5 caracteres    
        elif len(password1) < 5:
            raise forms.ValidationError('Las contrasenias deben tener mas de 5 digitos')

        elif len(cedula) > 10:
            print('Entre en el if')
            raise forms.ValidationError('El campo de cedula solo permite hasta 10 numeros')

        elif len(telefono) > 10:
            raise forms.ValidationError('El campo de telefono solo permite hasta 10 numeros')

        elif User.objects.filter(cedula=cedula).exists():
            print('entre en el if User')
            raise forms.ValidationError("Esta cedula ya a sido registrada")
        
        elif User.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya a sido registrado")
            
        elif User.objects.filter(telefono=telefono).exists():
            raise forms.ValidationError("Este telefono ya a sido registrado")
        
        return self.cleaned_data

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


class UserRegisterFormVeterinario(forms.ModelForm):

    #Aqui es donde se piden las contrasenias de forma mas segura
    password1 = forms.CharField(
        label = 'Contrasenia',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    cedula = forms.CharField(
    required=True,
    widget=forms.NumberInput(
        attrs={
                'placeholder':'Digite su cedula'
            }
        )
    )

    telefono = forms.CharField(
        required=True,
        widget=forms.NumberInput(
        )
    )

    def clean(self):
        cleaned_data = super(UserRegisterFormVeterinario, self).clean
        cedula = self.cleaned_data['cedula']
        telefono = self.cleaned_data['telefono']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        correo = self.cleaned_data['correo']

        if password1 != password2:
            raise forms.ValidationError('Las contrasenias no son iguales')

        #Verificando que la contrasenia tenga mas de 5 caracteres    
        elif len(password1) < 5:
            raise forms.ValidationError('Las contrasenias deben tener mas de 5 digitos')

        elif len(cedula) > 10:
            print('Entre en el if')
            raise forms.ValidationError('El campo de cedula solo permite hasta 10 numeros')

        elif len(telefono) > 10:
            raise forms.ValidationError('El campo de telefono solo permite hasta 10 numeros')

        elif User.objects.filter(cedula=cedula).exists():
            print('entre en el if vendedor')
            raise forms.ValidationError("Esta cedula ya a sido registrada")
        
        elif User.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya a sido registrado")
            
        elif User.objects.filter(telefono=telefono).exists():
            raise forms.ValidationError("Este telefono ya a sido registrado")
        
        return self.cleaned_data

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
        cleaned_data = super(LoginForm, self).clean
        cedula = self.cleaned_data['cedula']
        password = self.cleaned_data['password']

        if not authenticate(cedula = cedula, password= password):
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return self.cleaned_data


#Form de agregar una vista