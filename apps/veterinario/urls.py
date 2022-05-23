from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewHistorial.as_view(),name='historial'),

]