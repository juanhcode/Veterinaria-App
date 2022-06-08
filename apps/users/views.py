from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView,FormView, View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .forms import LoginForm, UserRegisterFormVendedor

from .models import Vendedor

from apps.ventas.models import Producto

from django.urls import reverse_lazy, reverse

# Create your views here.

#para crear superusuarios se utiliza el FormView ya que esta clase de usuarios es mas exigente
class VendedorRegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterFormVendedor
    success_url = '/'

    def form_valid(self,form):

        #creando usuario
        vendedor = Vendedor.objects.create_user(
            form.cleaned_data['cedula'],
            form.cleaned_data['correo'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            apellidos = form.cleaned_data['apellidos'],
            fecha_ingreso = form.cleaned_data['fecha_ingreso'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            telefono = form.cleaned_data['telefono'],
            tipo_usuario = form.cleaned_data['tipo_usuario'],
        )
        #Recuperando el permiso
        
        content_type = ContentType.objects.get_for_model(Producto)
        permission = Permission.objects.get(
            codename = 'view_producto',
            content_type = content_type
        )
        permission2 = Permission.objects.get(
            codename = 'add_producto',
            content_type = content_type
        )
        permission3 = Permission.objects.get(
            codename = 'change_producto',
            content_type = content_type
        )
        permission4 = Permission.objects.get(
            codename = 'delete_producto',
            content_type = content_type
        )
        vendedor.user_permissions.add(permission,permission2, permission3, permission4)

        return super(VendedorRegisterView, self).form_valid(form)

#Iniciando sesion
class LoginUser(FormView):
    template_name = 'user/inicio.html'
    form_class = LoginForm
    success_url = reverse_lazy('veterinaria_app:home')

    def form_valid(self,form):

        #autenticando el usuario
        user = authenticate(
            cedula = form.cleaned_data['cedula'],
            password = form.cleaned_data['password']
        )
        login (self.request, user)

        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    
    def get(self,request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )   
        )


# Vista de Admin-Menu
class ListViewAdministrador(TemplateView):
    template_name = 'administrador/home.html'

class ListViewRegistrarUsuarios(TemplateView):
    template_name = 'administrador/registrarUsuarios.html'

class ListViewVerUsuarios(TemplateView):
    template_name = 'administrador/verTablaUsuarios.html'
