from multiprocessing import context
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, DeleteView, UpdateView, FormView, View, CreateView

from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Carro, Pedido, Producto, ProductoCarro

from django.contrib.messages.views import SuccessMessageMixin

from .forms import FacturaForm, ProductoRegisterForm

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context
# Create your views here.

#Views del apartado ventas


class ProductoCreateView(PermissionRequiredMixin, SuccessMessageMixin, FormView):
    form_class = ProductoRegisterForm
    template_name = 'ventas/formulario.html'
    success_url = '.'
    permission_required = 'ventas.add_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')
    success_message = 'El registro fue agregado con exito'

    #validacion de los datos
    def form_valid(self, form):
        
        Producto.objects.create(
            identificacion = form.cleaned_data['identificacion'],
            nombre = form.cleaned_data['nombre'],
            descripcion = form.cleaned_data['descripcion'],
            precio = form.cleaned_data['precio'],
            iva = form.cleaned_data['iva'],
            stock = form.cleaned_data['stock'],
            vendedor = form.cleaned_data['vendedor'],
        )
    
        return super(ProductoCreateView, self).form_valid(form)
    

class ListaProductosViewTrg(PermissionRequiredMixin, ListView):
    template_name = 'ventas/ventas.html'
    model = Producto
    paginate_by = 5
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


class FacturasView(PermissionRequiredMixin, ListView):
    template_name = 'ventas/facturas.html'
    model = Pedido
    paginate_by = 5
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Pedido.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            cedula__icontains=palabra_clave
        )
        return lista

class Error403View(TemplateView):
    template_name = 'ventas/error403.html'


#------------------------------------------------Logica carrito de ventas/facturacion ----------------------------------

class AgregarAlCarro(PermissionRequiredMixin, TemplateView):
    template_name = 'ventas/agregarCarro.html'
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

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


class EditarCarroView(PermissionRequiredMixin, View):

    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

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




class CarroView(PermissionRequiredMixin, TemplateView):
    template_name = 'ventas/mycart.html'
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Carro.objects.get(id=cart_id)
        else:
            cart = None

        context['carro'] = cart     
        return context


class FacturacionView(PermissionRequiredMixin, CreateView):
    template_name = 'ventas/facturacion.html'
    form_class = FacturaForm
    success_url = reverse_lazy('ventas_app:ventas')
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

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

#Top 10 productos mas vendidos
class Reporte10PMV(PermissionRequiredMixin, View):

    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get(self, request, *args, **kwargs):

        sqlquery = ''' select vp.id, vp.nombre, sum(vpc.cantidad)
            from ventas_productocarro vpc inner join ventas_producto vp on vpc.producto_id = vp.id
            group by vp.id, vp.nombre
            order by sum(vpc.cantidad) desc limit 10
        '''

        productocarro = ProductoCarro.objects.raw(sqlquery)


        try:
            template = get_template('ventas/reporteProductoPDF.html')
            context = {'title':'Top 10 Productos mas vendidos', 'productocarro':productocarro}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('veterinaria_app:home'))


#Top 10 personas con mas compras
class Reporte10PMC(PermissionRequiredMixin, View):

    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get(self, request, *args, **kwargs):

        sqlquery = ''' select count(cedula), pedido_por, 1 as id
        from ventas_pedido
        group by cedula, pedido_por
        order by count(cedula) desc limit 10
        '''

        compradores = Pedido.objects.raw(sqlquery)


        
        template = get_template('ventas/reporteCompradorPDF.html')
        context = {'title':'Top 10 Clientes con mas compras', 'compradores':compradores}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        # create a pdf
        pisa_status = pisa.CreatePDF(
           html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
           return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


class ReporteRangoFechas(PermissionRequiredMixin, ListView):
    template_name = 'ventas/reporteRangoFechas.html'
    context_object_name = 'fechas'
    permission_required = 'ventas.view_producto'
    permission_denied_message = 'No tienes permisos'
    login_url = reverse_lazy('user_app:login')

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword",'')

        #fecha1
        f1 = self.request.GET.get("fecha1",'')

        #fecha2
        f2 = self.request.GET.get("fecha2",'')
        
        if f1 and f2:
            return Pedido.objects.listar_fechas(palabra_clave, f1, f2)

        else:
            return Pedido.objects.listar_fechas_default(palabra_clave)


#Reporte de ragos a pdf
# class ReporteRangoPDF(View):

#     def get(self, request, *args, **kwargs):

#         template = get_template('ventas/reporteRangoFechas.html')
#         context = {'title':'Rango Fechas'}
#         html = template.render(context)
#         response = HttpResponse(content_type='application/pdf')
#         # create a pdf
#         pisa_status = pisa.CreatePDF(
#            html, dest=response)
#         # if error then show some funny view
#         if pisa_status.err:
#            return HttpResponse('We had some errors <pre>' + html + '</pre>')
#         return response
        

