import pytest
from apps.veterinario.admin import admin
from apps.veterinario.models import HistorialClinico


def agregar_modelo(modelo):

    if modelo == HistorialClinico:
        return  admin.site.register(modelo)
    else:
        print('error no es el modelo')

def test_answer():
    assert agregar_modelo(HistorialClinico) == admin.site.register(HistorialClinico)
    
