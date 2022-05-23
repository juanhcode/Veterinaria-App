from django.urls import path
from . import views

app_name = 'ventas_app'
urlpatterns = [
    path('inventario/',views.ListaProductosView.as_view(),name='ventas'),
    path('formulario/',views.ProductoCreateView.as_view(),name='formulario'),
    path('update/<pk>/',views.ProductoUpdateView.as_view(),name='update'),
    path('delete/<pk>/',views.ProductoDeleteView.as_view(),name='delete'),

]