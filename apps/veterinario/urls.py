from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewHistorial.as_view(),name='historial'),
    path('ventas/',views.ListViewVentas.as_view(),name='ventas'),
    path('login/',views.ListViewLogin.as_view(),name='login'),

]