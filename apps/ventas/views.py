from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView, CreateView, ListView

from .models import Producto
# Create your views here.

#Views del apartado ventas


class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'ventas/formulario.html'
    #fields = ['first_name','last_name','job']
    fields = ['nombre', 'apellidos']

    #validacion de los datos
    def form_valid(self, form):
        producto = form.save()
    
        return super(ProductoCreateView, self).form_valid(form)
    success_url = ('/')

class ListaProductosView(ListView):
    template_name = 'ventas/ventas.html'
    model = Producto
=======
from django.views.generic import TemplateView
# Create your views here.

#Views del apartado ventas
class ViewVentas(TemplateView):
    template_name = 'ventas/ventas.html'
>>>>>>> 3618d22738bd3e12c85848d3bd5fe5a409ec2566
