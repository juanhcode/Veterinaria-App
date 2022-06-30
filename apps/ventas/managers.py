from django.db import models
from django.contrib.postgres.search import TrigramSimilarity


class VentasManager(models.Manager):

    #trabajando con Tiagram 
    def listar_producto_trg(self, kword):

        if kword:
            resultado = self.filter(
            nombre__trigram_similar = kword
        )
            return resultado
        else:
            return self.all()

    #Listar rango de fechas
    def listar_fechas(self, kword, fecha1, fecha2):

        resultado = self.filter(
            pedido_por__icontains=kword,
            creado_el__range=(fecha1,fecha2)
        )
        return resultado

    def listar_fechas_default(self, kword):
        self.all()
    


