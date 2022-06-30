from django.db import models

from apps.users.models import Veterinario, Mascota

# Create your models here.

class HistorialClinico(models.Model):

    anamnesis = models.TextField('Anamnesis')
    patologia = models.TextField('Patologia')
    peso = models.PositiveIntegerField('Peso')
    examen_fisico = models.TextField('Examen Fisico')
    frecuencia_cardiaca = models.PositiveIntegerField('Frecuencia Cardiaca')
    diagnostico = models.TextField('Diagnostico')
    vacunas = models.TextField('Vacunas')
    tratamiento = models.TextField('Tratamiento')
    temperatura = models.PositiveIntegerField('Temperatura')
    detalles_visita = models.TextField('Detalles de la Visita')
    fecha_creacion = models.DateField(auto_now_add=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)


    class Meta:
        db_table = 'historialclinico'
        verbose_name = 'Historial Clinico'
        verbose_name_plural = 'Historiales Clinicos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.mascota) + ' ' + str(self.veterinario) + ' ' + 'Fecha de creacion: ' + str(self.fecha_creacion)