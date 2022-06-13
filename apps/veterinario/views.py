from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class ListViewVeterinario(LoginRequiredMixin, TemplateView):
    template_name = 'veterinaria/home.html'
    login_url = reverse_lazy('user_app:login')

class ListViewHistorial(TemplateView):
    template_name = 'historial/historial.html'

