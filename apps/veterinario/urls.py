from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewHistorial.as_view(),name='historial'),
    path('login/',views.ListViewLogin.as_view(),name='login'),
    path('inicio-historial/',views.ListViewInicioHistorial.as_view(),name='inicio-historial'),
    path('cliente-responsable/',views.ListViewClienteResponsable.as_view(),name='cliente-responsable'),

]