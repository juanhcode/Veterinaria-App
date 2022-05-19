from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from .models import Producto
# Create your views here.

#Views del apartado ventas


class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'ventas/agregar.html'
    #fields = ['first_name','last_name','job']
    fields = ('__all__')

    #validacion de los datos
    def form_valid(self, form):
        producto = form.save()
    
        return super(ProductoCreateView, self).form_valid(form)
    success_url = ('.')

class ListaProductosView(ListView):
    template_name = 'ventas/ventas.html'
    model = Producto

class TemplateView(TemplateView):
    template_name = 'ventas/formulario.html'