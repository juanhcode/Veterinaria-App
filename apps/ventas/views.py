from tkinter.tix import Select
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, DeleteView, UpdateView, FormView

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Carro, Producto, ProductoCarro

from apps.users.models import Duenio, Vendedor

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

class FacturasFormularioView(PermissionRequiredMixin, FormView):
    template_name = 'ventas/formularioFactura.html'
    success_url = reverse_lazy('ventas_app:facturas')
    permission_required = 'ventas.add_factura'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def form_valid(self, form):
        
        form.save()
    
        return super(FacturasFormularioView, self).form_valid(form)


class AgregarAlCarro(TemplateView):
    template_name = 'ventas/agregarCarro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtener id del producto desde la peticion de url
        product_id = self.kwargs['pro_id']

        #obtener el producto
        product_obj = Producto.objects.get(id=product_id)

        #comprobar si el carro existe
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Carro.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.productocarro_set.filter(producto=product_obj)

            #producto ya existente en el carro
            if this_product_in_cart.exists():
                productocarro= this_product_in_cart.last()
                productocarro.cantidad += 1
                productocarro.subtotal += product_obj.precio
                productocarro.save()
                cart_obj.total += product_obj.precio
                cart_obj.save()
                
            #nuevo producto es agregado en el carro
            else:
                productocarro = ProductoCarro.objects.create(
                    carro=cart_obj, producto=product_obj, rate=product_obj.precio, cantidad=1,
                    subtotal=product_obj.precio
                )
                cart_obj.total += product_obj.precio
                cart_obj.save()
        else:
            cart_obj = Carro.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            productocarro = ProductoCarro.objects.create(
                    carro=cart_obj, producto=product_obj, rate=product_obj.precio, cantidad=1,
                    subtotal=product_obj.precio
                )
            cart_obj.total += product_obj.precio
            cart_obj.save()
           
        return context 