from django.urls import path
from . import views

app_name = 'ventas_app'
urlpatterns = [
    path('ventas/',views.ViewVentas.as_view(),name='ventas'),

]