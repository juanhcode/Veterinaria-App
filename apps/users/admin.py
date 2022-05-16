from curses.ascii import US
from django.contrib import admin

from .models import User, Veterinario, Vendedor

# Register your models here.

admin.site.register(User)
admin.site.register(Veterinario)
admin.site.register(Vendedor)