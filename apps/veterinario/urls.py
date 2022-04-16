from django.urls import path
from . import views

app_name = 'veterinaria_app'
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewVeterinario.as_view(),name='historial'),
]