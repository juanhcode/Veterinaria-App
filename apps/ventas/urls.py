from django.urls import path
from . import views

app_name = 'ventas_app'
urlpatterns = [
    path('ventas/',views.ListaProductosView.as_view(),name='ventas'),
    path('formulario/',views.ProductoCreateView.as_view(),name='formulario'),
    path('formularioprueba/',views.TemplateView.as_view(),name='formularioPrueba'),
]