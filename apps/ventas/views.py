from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, FormView

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .models import Producto

from apps.users.models import Vendedor

from .forms import ProductoRegisterForm
# Create your views here.

#Views del apartado ventas


class ProductoCreateView(PermissionRequiredMixin, FormView):
    form_class = ProductoRegisterForm
    template_name = 'ventas/formulario.html'
    success_url = reverse_lazy('ventas_app:ventas')
    permission_required = 'ventas.add_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    #validacion de los datos
    def form_valid(self, form):
        
        form.save()
    
        return super(ProductoCreateView, self).form_valid(form)
    

class ListaProductosViewTrg(PermissionRequiredMixin, ListView):
    template_name = 'ventas/ventas.html'
    paginate_by = 3
    ordering = 'nombre'
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")

        
        return Producto.objects.listar_producto_trg(palabra_clave)


class ProductoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Producto
    template_name = "ventas/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('ventas_app:ventas')
    permission_required = 'ventas.change_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')


class ProductoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('ventas_app:ventas')
    permission_required = 'ventas.delete_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')





class Error403View(TemplateView):
    template_name = 'ventas/error403.html'

class FacturasView(TemplateView):
    template_name = 'ventas/facturas.html'

class FacturasFormularioView(TemplateView):
    template_name = 'ventas/formularioFactura.html'