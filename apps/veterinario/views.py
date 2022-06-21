from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, ListView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.veterinario.models import HistorialClinico

from .forms import HistorialRegisterForm, MascotaRegisterForm, ResponsableRegisterForm

from apps.users.models import Duenio, Mascota

# Create your views here.

class ListViewVeterinario(LoginRequiredMixin, TemplateView):
    template_name = 'veterinaria/home.html'
    login_url = reverse_lazy('user_app:login')

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'

class ListViewHistorial(PermissionRequiredMixin, ListView):
    template_name = 'historial/historial.html'
    paginate_by = 3
    ordering = 'mascota'
    model = HistorialClinico
    permission_required = 'users.view_historialclinico'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class CreateFormularioHistorial(PermissionRequiredMixin, FormView):
    template_name = 'historial/formulario-historial.html'
    form_class = HistorialRegisterForm
    success_url = reverse_lazy('veterinaria_app:historial')
    permission_required = 'users.create_historialclinico'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def form_valid(self,form):

        #creando usuario
        HistorialClinico.objects.create(
            anamnesis = form.cleaned_data['anamnesis'],
            patologia = form.cleaned_data['patologia'],
            peso = form.cleaned_data['peso'],
            examen_fisico = form.cleaned_data['examen_fisico'],
            frecuencia_cardiaca = form.cleaned_data['frecuencia_cardiaca'],
            diagnostico = form.cleaned_data['diagnostico'],
            vacunas = form.cleaned_data['vacunas'],
            tratamiento = form.cleaned_data['tratamiento'],
            temperatura = form.cleaned_data['temperatura'],
            detalles_visita = form.cleaned_data['detalles_visita'],
            veterinario = form.cleaned_data['veterinario'],
            mascota = form.cleaned_data['mascota'],
        )

        return super(CreateFormularioHistorial, self).form_valid(form)

class ListViewInicioHistorial(PermissionRequiredMixin, TemplateView):
    template_name = 'historial/inicio-historial.html'
    permission_required = 'users.view_historialclinico'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

class ListViewVerClienteResponsable(PermissionRequiredMixin, ListView):
    template_name = 'historial/cliente-responsable.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Duenio
    permission_required = 'users.view_duenio'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

class CreateClienteResponsable(PermissionRequiredMixin, FormView):
    template_name = 'historial/formulario-clientes.html'
    form_class = ResponsableRegisterForm
    success_url = reverse_lazy('veterinaria_app:cliente-responsable')
    permission_required = 'users.add_duenio'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def form_valid(self,form):

        #creando usuario
        Duenio.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellidos = form.cleaned_data['apellidos'],
            cedula = form.cleaned_data['cedula'],
            direccion = form.cleaned_data['direccion'],
            edad = form.cleaned_data['edad'],
            sexo = form.cleaned_data['sexo'],
            telefono = form.cleaned_data['telefono'],
        )

        return super(CreateClienteResponsable, self).form_valid(form)
    

class ListViewMascotas(PermissionRequiredMixin, ListView):
    template_name = 'historial/mascotas.html'
    paginate_by = 3
    ordering = 'nombre'
    model = Mascota
    permission_required = 'users.view_mascota'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class CreateFormularioMascotas(PermissionRequiredMixin, FormView):
    template_name = 'historial/formulario-mascota.html'
    form_class = MascotaRegisterForm
    success_url = reverse_lazy('veterinaria_app:mascotas')
    permission_required = 'users.add_mascota'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def form_valid(self,form):

        #creando usuario
        Mascota.objects.create(
            raza = form.cleaned_data['raza'],
            estado = form.cleaned_data['estado'],
            color = form.cleaned_data['color'],
            especie = form.cleaned_data['especie'],
            edad = form.cleaned_data['edad'],
            nombre = form.cleaned_data['nombre'],
            castrado = form.cleaned_data['castrado'],
            sexo = form.cleaned_data['sexo'],
            duenio = form.cleaned_data['duenio'],
        )

        return super(CreateFormularioMascotas, self).form_valid(form)
