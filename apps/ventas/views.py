from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#Views del apartado ventas
class ViewVentas(TemplateView):
    template_name = 'ventas/ventas.html'