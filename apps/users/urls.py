from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    
    path('login-user/',views.LoginUser.as_view(),name='login'),
    path('registrar-vendedor/',views.VendedorRegisterView.as_view(),name='registrar-vendedor'),
    path('registrar-veterinario/',views.VeterinarioRegisterView.as_view(),name='registrar-veterinario'),
    path('registrar-admin/',views.AdminRegisterView.as_view(),name='registrar-admin'),
    path('logout/',views.LogoutView.as_view(),name='logout'),

    path('delete/<pk>/',views.VendedorDeleteView.as_view(),name='delete-vendedor'),
    
    path('administrador/',views.ListViewAdministrador.as_view(),name='administrador'),
    path('registrarUsuariosHome/',views.HomeRegistrarUsuarios.as_view(),name='registrarUsuariosHome'),
    path('home-listado/',views.HomeVerUsuarios.as_view(),name='homeListado'),
    path('ver-admins/',views.ListViewVerAdmins.as_view(),name='verAdmins'),

]