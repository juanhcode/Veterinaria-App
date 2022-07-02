from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import TemplateView,FormView, View, DeleteView, ListView, UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin


from .forms import LoginForm, UserRegisterFormAdministrador, UserRegisterFormVendedor, UserRegisterFormVeterinario

from .models import Administrador, Vendedor, Veterinario
from apps.veterinario.models import HistorialClinico


from apps.ventas.models import Producto

from django.urls import reverse_lazy, reverse

# Create your views here.

class HomeRegistrarUsuarios(PermissionRequiredMixin, TemplateView):
    template_name = 'administrador/home-registrar.html'
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


# Vista de Admin-Menu
class ListViewAdministrador(PermissionRequiredMixin ,TemplateView):
    template_name = 'administrador/home.html'
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class HomeVerUsuarios(PermissionRequiredMixin, TemplateView):
    template_name = 'administrador/listado_usuarios_home.html'
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


#para crear superusuarios se utiliza el FormView ya que esta clase de usuarios es mas exigente
class VendedorRegisterView(PermissionRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'administrador/admin_vendedor.html'
    form_class = UserRegisterFormVendedor
    success_url = '.'
    permission_required = 'users.add_vendedor'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
    success_message = 'El registro fue agregado con exito'

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
class VeterinarioRegisterView(PermissionRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'administrador/admin_veterinario.html'
    form_class = UserRegisterFormVeterinario
    success_url = '.'
    permission_required = 'users.add_veterinario'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
    success_message = 'El registro fue agregado con exito'

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
class AdminRegisterView(PermissionRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'administrador/admin_admin.html'
    form_class = UserRegisterFormAdministrador
    success_url = '.'
    permission_required = 'users.add_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
    success_message = 'El registro fue agregado con exito'

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

class ListViewReporteUsuarios(PermissionRequiredMixin, TemplateView):
    template_name = 'administrador/reporteAdmin.html'
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class ListViewVerAdmins(PermissionRequiredMixin, ListView):
    template_name = 'administrador/verAdmins.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Administrador
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Administrador.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            cedula__icontains=palabra_clave
        )
        return lista


class AdminUpdateView(PermissionRequiredMixin, UpdateView):
    model = Administrador
    template_name = "administrador/actualizar_admin.html"
    fields = (
        'cedula',
        'nombre',
        'apellidos',
        'edad',
        'sexo',
        'telefono',
        'correo',
        'fecha_ingreso'
    )
    success_url = reverse_lazy('user_app:verAdmins')
    permission_required = 'users.change_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class AdminDeleteView(PermissionRequiredMixin, DeleteView):
    model = Administrador
    success_url = reverse_lazy('user_app:verAdmins')
    permission_required = 'users.delete_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class ListViewVerVendedores(PermissionRequiredMixin, ListView):
    template_name = 'administrador/verVendedor.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Vendedor
    permission_required = 'users.view_vendedor'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Vendedor.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            cedula__icontains=palabra_clave
        )
        return lista

class VendedorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Vendedor
    template_name = "administrador/actualizar_vendedor.html"
    fields = (
        'cedula',
        'nombre',
        'apellidos',
        'edad',
        'sexo',
        'telefono',
        'correo',
        'fecha_ingreso'
    )
    success_url = reverse_lazy('user_app:verVendedor')
    permission_required = 'users.change_vendedor'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class VendedorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('user_app:verVendedor')
    permission_required = 'users.delete_vendedor'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class ListViewVerVeterinario(PermissionRequiredMixin, ListView):
    template_name = 'administrador/verVeterinario.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Veterinario
    permission_required = 'users.view_veterinario'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Veterinario.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            cedula__icontains=palabra_clave
        )
        return lista


class VeterinarioUpdateView(PermissionRequiredMixin, UpdateView):
    model = Veterinario
    template_name = "administrador/actualizar_veterinario.html"
    fields = (
        'cedula',
        'nombre',
        'apellidos',
        'edad',
        'sexo',
        'telefono',
        'correo',
        'fecha_ingreso',
        'titulo'
    )
    success_url = reverse_lazy('user_app:verVeterinario')
    permission_required = 'users.change_veterinario'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class VeterinarioDeleteView(PermissionRequiredMixin, DeleteView):
    model = Veterinario
    success_url = reverse_lazy('user_app:verVeterinario')
    permission_required = 'users.delete_veterinario'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
