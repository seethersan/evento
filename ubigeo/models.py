from django.db import models, migrations
from django.db.models import Count

# Create your models here.
class Pais(models.Model):
    codigo = models.CharField(max_length=2, verbose_name='Código de País')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de País')

    def __str__(self):
        return self.nombre

    def ubicacion(self):
        resultado = self.ubicacion_set.aggregate(Count('nombre'))
        return resultado['nombre__count']

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'


