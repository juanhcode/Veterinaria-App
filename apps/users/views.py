from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import TemplateView,FormView, View, DeleteView, ListView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .forms import LoginForm, UserRegisterFormAdministrador, UserRegisterFormVendedor, UserRegisterFormVeterinario

from .models import Administrador, Vendedor, Veterinario
from apps.veterinario.models import HistorialClinico

from apps.ventas.models import Producto

from django.urls import reverse_lazy, reverse

# Create your views here.

class HomeRegistrarUsuarios(TemplateView):
    template_name = 'administrador/home-registrar.html'


# Vista de Admin-Menu
class ListViewAdministrador(TemplateView):
    template_name = 'administrador/home.html'


class HomeVerUsuarios(TemplateView):

    template_name = 'administrador/listado_usuarios_home.html'


#para crear superusuarios se utiliza el FormView ya que esta clase de usuarios es mas exigente
class VendedorRegisterView(FormView):
    template_name = 'administrador/admin_vendedor.html'
    form_class = UserRegisterFormVendedor
    success_url = '.'

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


#Registrando veterinario
class VeterinarioRegisterView(FormView):
    template_name = 'administrador/admin_veterinario.html'
    form_class = UserRegisterFormVeterinario
    success_url = '.'

    def form_valid(self,form):

        #creando usuario
        veterinario = Veterinario.objects.create_user(
            form.cleaned_data['cedula'],
            form.cleaned_data['correo'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            apellidos = form.cleaned_data['apellidos'],
            fecha_ingreso = form.cleaned_data['fecha_ingreso'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            telefono = form.cleaned_data['telefono'],
            titulo = form.cleaned_data['titulo'],
        )
        #Recuperando el permiso
        
        content_type = ContentType.objects.get_for_model(HistorialClinico)
        permission = Permission.objects.get(
            codename = 'view_historialclinico',
            content_type = content_type
        )
        permission2 = Permission.objects.get(
            codename = 'add_historialclinico',
            content_type = content_type
        )
        permission3 = Permission.objects.get(
            codename = 'change_historialclinico',
            content_type = content_type
        )
        permission4 = Permission.objects.get(
            codename = 'delete_historialclinico',
            content_type = content_type
        )
        veterinario.user_permissions.add(permission,permission2, permission3, permission4)

        return super(VeterinarioRegisterView, self).form_valid(form)


#Registrando administrador
class AdminRegisterView(FormView):
    template_name = 'administrador/admin_admin.html'
    form_class = UserRegisterFormAdministrador
    success_url = '.'

    def form_valid(self,form):

        #creando usuario
        Administrador.objects.create_superuser(
            form.cleaned_data['cedula'],
            form.cleaned_data['correo'],
            form.cleaned_data['password1'],
            nombre = form.cleaned_data['nombre'],
            apellidos = form.cleaned_data['apellidos'],
            fecha_ingreso = form.cleaned_data['fecha_ingreso'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            telefono = form.cleaned_data['telefono'],
        )

        return super(AdminRegisterView, self).form_valid(form)
    

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


class ListViewVerAdmins(ListView):
    template_name = 'administrador/verAdmins.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Administrador

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Administrador.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            cedula__icontains=palabra_clave
        )
        return lista


class ProductoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Producto
    template_name = "ventas/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('ventas_app:ventas')
    permission_required = 'ventas.change_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')




class VendedorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('user_app:verUsuarios')
    permission_required = 'users.delete_vendedor'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
