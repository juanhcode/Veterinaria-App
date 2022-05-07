from django.urls import path
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view()),
=======

app_name = 'veterinaria_app'
urlpatterns = [
    path('home/',views.ListViewVeterinario.as_view(),name='home'),
    path('historial/',views.ListViewHistorial.as_view(),name='historial'),
    path('login/',views.ListViewLogin.as_view(),name='login'),

>>>>>>> 78350140821da17f4691e2414e2a5caba8a1e666
]