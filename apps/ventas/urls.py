from django.urls import path
from . import views

app_name = 'ventas_app'
urlpatterns = [
    path('inventario/',views.ListaProductosViewTrg.as_view(),name='ventas'),
    path('formulario/',views.ProductoCreateView.as_view(),name='formulario'),
    path('update/<pk>/',views.ProductoUpdateView.as_view(),name='update'),
    path('delete/<pk>/',views.ProductoDeleteView.as_view(),name='delete'),
    path('facturas/',views.FacturasView.as_view(),name='facturas'),
    path('facturasFormulario/',views.FacturasFormularioView.as_view(),name='formularioFacturas'),

    path('add-to-cart-<int:pro_id>/',views.AgregarAlCarro.as_view(),name='agregarCarro'),
    path('my-cart/',views.CarroView.as_view(),name='MiCarro'),
    path('editar-carro/<int:cp_id>/',views.EditarCarroView.as_view(),name='EditarCarro'),
    path('empty-car/',views.VaciarCarroView.as_view(),name='VaciarCarro'),

    path('facturacion/',views.FacturacionView.as_view(),name='Facturacion'),

    path('reporte1/',views.Reporte10ProductosMasVendidos.as_view(),name='reporteUno'),
]