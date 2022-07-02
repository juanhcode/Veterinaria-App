import pytest

from apps.users.models import User, Vendedor

@pytest.mark.django_db
def test_crear_vendedor():
    vendedor = Vendedor.objects.create(
        nombre = 'test',
        apellidos = 'testapellido',
        cedula = '123456789',
        fecha_ingreso = '2020-04-12',
        edad = '24',
        sexo = 'M',
        correo = 'test@outlook.com',
        telefono = '3198317821',
    )
    assert vendedor.nombre == 'test'

@pytest.mark.django_db
def test_crear_user():
    user = User.objects.create_superuser(
        nombre = 'test2',
        apellidos = 'testapellido2',
        cedula = '123456289',
        fecha_ingreso = '2020-04-12',
        edad = '44',
        sexo = 'F',
        correo = 'test2@outlook.com',
        telefono = '3148317821',
    )
    assert user.is_superuser