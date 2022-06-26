from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class ListViewVeterinario(LoginRequiredMixin, TemplateView):
    template_name = 'veterinaria/home.html'
    login_url = reverse_lazy('user_app:login')

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

class ListViewFormularioHistorial(TemplateView):
    template_name = 'historial/formulario-historial.html'

class ListViewInicioHistorial(TemplateView):
    template_name = 'historial/inicio-historial.html'

class ListViewClienteResponsable(TemplateView):
    template_name = 'historial/cliente-responsable.html'

class ListViewFormularioClienteResponsable(TemplateView):
    template_name = 'historial/formulario-clientes.html'

class ListViewMascotas(TemplateView):
    template_name = 'historial/mascotas.html'

class ListViewFormularioMascotas(TemplateView):
    template_name = 'historial/formulario-mascota.html'

class DetailViewHistorial(TemplateView):
    template_name = 'historial/detailView.html'