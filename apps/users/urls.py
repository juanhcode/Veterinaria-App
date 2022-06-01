from django.urls import path
from . import views

app_name = 'user_app'
urlpatterns = [
    path('administrador/',views.ListViewAdministrador.as_view(),name='administrador'),
    path('login-user/',views.LoginUser.as_view(),name='login'),
    path('register/',views.VendedorRegisterView.as_view(),name='register'),
    
    path('registrarAdmin/',views.ListViewRegistrarAdmin.as_view(),name='registrarAdmin'),
    path('registrarVeterinario/',views.ListViewRegistrarVeterinario.as_view(),name='registrarVeterinario'),
    
]