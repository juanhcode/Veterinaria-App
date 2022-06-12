from curses.ascii import US
from django.contrib import admin

from .models import Veterinario, Vendedor, Duenio, Mascota, Administrador

# Register your models here.
admin.site.register(Administrador)
admin.site.register(Veterinario)
admin.site.register(Vendedor)
admin.site.register(Duenio)
admin.site.register(Mascota)