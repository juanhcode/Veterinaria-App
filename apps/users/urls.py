from django.urls import path
from . import views

app_name = 'user_app'
urlpatterns = [
    path('administrador/',views.ListViewAdministrador.as_view(),name='administrador'),
    path('login-user/',views.LoginUser.as_view(),name='login'),
    path('register/',views.VendedorRegisterView.as_view(),name='register'),
    
    path('registrarUsuario/',views.ListViewRegistrarUsuario.as_view(),name='registrarUsuario'),
    
]