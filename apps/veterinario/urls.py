from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewHistorial.as_view(),name='historial'),
    path('formulario-historial/',views.CreateFormularioHistorial.as_view(),name='formulario-historial'),
    path('inicio-historial/',views.ListViewInicioHistorial.as_view(),name='inicio-historial'),
    path('cliente-responsable/',views.ListViewVerClienteResponsable.as_view(),name='cliente-responsable'),
    path('formulario-cliente/',views.CreateClienteResponsable.as_view(),name='formulario-cliente'),
    path('mascotas/',views.ListViewMascotas.as_view(),name='mascotas'),
    path('formulario-mascota/',views.CreateFormularioMascotas.as_view(),name='formulario-mascota'),
    path('detalle-historial/<pk>/',views.DetailViewHistorial.as_view(),name='detailView'),

]