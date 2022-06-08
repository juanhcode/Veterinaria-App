from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    
    path('login-user/',views.LoginUser.as_view(),name='login'),
    path('register/',views.VendedorRegisterView.as_view(),name='register'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    
    path('administrador/',views.ListViewAdministrador.as_view(),name='administrador'),
    path('registrarUsuarios/',views.ListViewRegistrarUsuarios.as_view(),name='registrarUsuarios'),
    path('verUsuarios/',views.ListViewVerUsuarios.as_view(),name='verUsuarios'),

]