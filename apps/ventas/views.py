from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, DeleteView, UpdateView, FormView, View, CreateView

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Carro, Producto, ProductoCarro

from apps.users.models import Duenio, Vendedor

from .forms import FacturaForm, ProductoRegisterForm
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
    # success_url = reverse_lazy('ventas_app:facturas')
    # permission_required = 'ventas.add_factura'
    # permission_denied_message = 'No tienes permisos'
    # login_url = reverse_lazy('user_app:login')

    # def form_valid(self, form):
        
    #     form.save()
    
    #     return super(FacturasFormularioView, self).form_valid(form)

#------------------------------------------------Logica carrito de ventas/facturacion ----------------------------------

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


class EditarCarroView(View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs['cp_id']
        action = request.GET.get("action")
        cp_obj = ProductoCarro.objects.get(id=cp_id)
        cart_obj = cp_obj.carro
        
        if action == 'inc':
            cp_obj.cantidad += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == 'dcr':
            cp_obj.cantidad -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.cantidad == 0:
                cp_obj.delete()

        elif action == 'rmv':
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()

        else:
            pass
        return redirect('ventas_app:MiCarro')


class VaciarCarroView(View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Carro.objects.get(id=cart_id)
            cart.productocarro_set.all().delete()
            cart.total = 0
            cart.save()

        return redirect('ventas_app:MiCarro')




class CarroView(TemplateView):
    template_name = 'ventas/mycart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Carro.objects.get(id=cart_id)
        else:
            cart = None

        context['carro'] = cart     
        return context


class FacturacionView(CreateView):
    template_name = 'ventas/facturacion.html'
    form_class = FacturaForm
    success_url = reverse_lazy('ventas_app:ventas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Carro.objects.get(id=cart_id)
        else:
            cart_obj = None

        context['carro'] = cart_obj

        return context

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = Carro.objects.get(id=cart_id)
            form.instance.carro = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.descuento = 0
            form.instance.total = cart_obj.total
            del self.request.session['cart_id']
        else:
            return redirect('ventas_app:ventas')
        return super().form_valid(form)

#------------------------------------------Fin Logica carrito de ventas/facturacion----------------------------------


#------------------------------------------Modulo de reportes--------------------------------------------------------

class Reporte10ProductosMasVendidos(PermissionRequiredMixin, ListView):
    template_name = 'ventas/reporteProducto.html'
    permission_required = 'users.view_administrador'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    #Modulo de reporte 10 productos mas vendidos
    def get_queryset(self):

        sqlquery = "select count(vp.id), vp.nombre, vp.id from ventas_productocarro vpc inner join ventas_producto vp on vpc.producto_id = vp.id group by vp.nombre, vp.id"
        

        return ProductoCarro.objects.raw(sqlquery)


