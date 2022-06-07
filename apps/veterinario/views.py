from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

class ListViewInicioHistorial(TemplateView):
    template_name = 'historial/inicio-historial.html'

class ListViewClienteResponsable(TemplateView):
    template_name = 'historial/cliente-responsable.html'

class ListViewFormularioClienteResponsable(TemplateView):
    template_name = 'historial/formulario-clientes.html'
