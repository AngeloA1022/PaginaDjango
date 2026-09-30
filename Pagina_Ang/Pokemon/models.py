from django.db import models


class Pokemon(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Nombre del Pokemon')
    Tipo = models.CharField(max_length=100, verbose_name='Tipo del Pokemon', blank=True, null=True)
    Descripcion = models.TextField(max_length=500, verbose_name='Descripción del Pokemon')
    Imagen = models.CharField(max_length=255, blank=True, null=True, verbose_name='Imagen del Pokemon')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'pokemon'
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'