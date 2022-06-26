from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    
    path('login-user/',views.LoginUser.as_view(),name='login'),
    path('registrar-vendedor/',views.VendedorRegisterView.as_view(),name='registrar-vendedor'),
    path('registrar-veterinario/',views.VeterinarioRegisterView.as_view(),name='registrar-veterinario'),
    path('registrar-admin/',views.AdminRegisterView.as_view(),name='registrar-admin'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    
    path('administrador/',views.ListViewAdministrador.as_view(),name='administrador'),
    path('registrarUsuariosHome/',views.HomeRegistrarUsuarios.as_view(),name='registrarUsuariosHome'),
    path('home-listado/',views.HomeVerUsuarios.as_view(),name='homeListado'),

    path('ver-admins/',views.ListViewVerAdmins.as_view(),name='verAdmins'),
    path('actualizar-admins/<pk>/',views.AdminUpdateView.as_view(),name='actualizarAdmins'),
    path('eliminar-admins/<pk>/',views.AdminDeleteView.as_view(),name='eliminarAdmins'),

    path('ver-vendedor/',views.ListViewVerVendedores.as_view(),name='verVendedor'),
    path('actualizar-vendedor/<pk>/',views.VendedorUpdateView.as_view(),name='actualizarVendedor'),
    path('eliminar-vendedor/<pk>/',views.VendedorDeleteView.as_view(),name='eliminarVendedor'),

    path('ver-veterinario/',views.ListViewVerVeterinario.as_view(),name='verVeterinario'),
    path('actualizar-veterinario/<pk>/',views.VeterinarioUpdateView.as_view(),name='actualizarVeterinario'),
    path('eliminar-veterinario/<pk>/',views.VeterinarioDeleteView.as_view(),name='eliminarVeterinario'),

    path('reporteUsuarios/',views.ListViewReporteUsuarios.as_view(),name='reporteUsuarios'),
]