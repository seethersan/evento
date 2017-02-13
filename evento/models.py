from django.db import models
from ubigeo.models import Pais
from usuarios.models import User

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de Evento')
    descripcion = models.TextField(verbose_name='Descripción de la Ubicación')
    direccion = models.CharField(max_length=100, verbose_name='Dirección de la Ubicación')
    latitud = models.FloatField(blank=True, null=True, verbose_name='Latitud de la Ubicación')
    longitud = models.FloatField(blank=True, null=True, verbose_name='Longitud de la Ubicación')
    pais = models.ForeignKey(Pais, verbose_name="País")
    usuario = models.ForeignKey(User, verbose_name="Organizador")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'