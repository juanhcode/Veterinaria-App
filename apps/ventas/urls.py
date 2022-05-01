from django.urls import path
from . import views

app_name = 'ventas_app'
urlpatterns = [
<<<<<<< HEAD
    path('ventas/',views.ListaProductosView.as_view(),name='ventas'),
    path('formulario/',views.ProductoCreateView.as_view(),name='formulario'),
=======
    path('ventas/',views.ViewVentas.as_view(),name='ventas'),
>>>>>>> 3618d22738bd3e12c85848d3bd5fe5a409ec2566

]