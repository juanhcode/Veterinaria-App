from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManagerVeterinaria(BaseUserManager, models.Manager):

    #aqui es donde se pasan los parametros con los que se creara un superusuario o un superusuario
    ''' esta funcion decide como crear los superusuarios segun los parametros que le enviemos por ejemplo:
    los usuarios normales tienen en su return dos False, es decir que no seran staff ni superusuarios  '''
    def _create_user(self, cedula, correo, password, is_staff, is_superuser,is_active, **extra_fields):
        user = self.model(
            cedula=cedula,
            correo = correo,
            is_staff=is_staff,
            is_superuser= is_superuser,
            is_active = is_active,
            **extra_fields
        )
        #encriptando el password
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, cedula, correo, password=None, **extra_fields):
        return self._create_user(cedula, correo, password, True, False, True, **extra_fields)

    def create_superuser(self, cedula, correo, password=None, **extra_fields):
        return self._create_user(cedula, correo, password, True, True,True, **extra_fields)


    #trabajando con Tiagram 
    def listar_producto_trg(self, kword):

        if kword:
            resultado = self.filter(
            nombre__trigram_similar = kword
        )
            return resultado
        else:
            return self.all()[:10]


