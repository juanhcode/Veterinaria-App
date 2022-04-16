from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewVeterinario.as_view(),name='historial'),
    path('ventas/',views.ListViewVentas.as_view(),name='ventas'),

]