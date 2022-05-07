from django.shortcuts import render
from django.views.generic import TemplateView
<<<<<<< HEAD
from django.http import HttpResponse
# Create your views here.
class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'
=======


# Create your views here.

class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

class ListViewLogin(TemplateView):
    template_name = 'login/Inicio.html'
>>>>>>> 78350140821da17f4691e2414e2a5caba8a1e666
