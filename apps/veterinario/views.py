from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.
class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'

class ListViewVentas(TemplateView):
    template_name = 'ventas/ventas.html'

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'