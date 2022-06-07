from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ListViewInicioHistorial(TemplateView):
    template_name = 'historial/inicio-historial.html'

class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'
