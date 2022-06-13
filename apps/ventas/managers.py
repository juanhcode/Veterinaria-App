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
            return self.all()[:10]

