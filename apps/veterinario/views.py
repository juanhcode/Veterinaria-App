from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ListViewVeterinario(TemplateView):
    template_name = 'veterinaria/home.html'
