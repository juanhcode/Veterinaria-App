from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, FormView

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Producto

from apps.users.models import Vendedor

from .forms import ProductoRegisterForm
# Create your views here.

#Views del apartado ventas


class ProductoCreateView(PermissionRequiredMixin, FormView):
    form_class = ProductoRegisterForm
    template_name = 'ventas/formulario.html'
    #context_object_name = 'productos'
    #fields = ['first_name','last_name','job']
    success_url = '/'
    permission_required = 'producto.view_producto'
    permission_denied_message = 'No tienes permisos'

    #validacion de los datos
    def form_valid(self, form):
        
        form.save()
        
        '''
        Producto.objects.create(
            form.cleaned_data['nombre'],
            form.cleaned_data['descripcion'],
            form.cleaned_data['precio'],
            form.cleaned_data['iva'],
            form.cleaned_data['stock'],
            form.cleaned_data['vendedor'],
        )'''
    
        return super(ProductoCreateView, self).form_valid(form)
    

class ListaProductosView(ListView):
    template_name = 'ventas/ventas.html'
    model = Producto


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "ventas/delete.html"
    success_url = reverse_lazy('ventas_app:ventas')


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "ventas/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('ventas_app:ventas')


class Error403View(TemplateView):
    template_name = 'ventas/error403.html'

class FacturasView(TemplateView):
    template_name = 'ventas/facturas.html'

class FacturasFormularioView(TemplateView):
    template_name = 'ventas/formularioFactura.html'