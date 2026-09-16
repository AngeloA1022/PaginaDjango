from django.db import models

# Create your models here.

class Pokemon(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Nombre del Pokemon')
    Tipo = models.CharField(max_length=100, verbose_name='Tipo del Pokemon')
    Descripcion = models.TextField(max_length=500, verbose_name='Descripción del Pokemon')
    Imagen = models.ImageField(upload_to='images/', verbose_name='Imagen del Pokemon')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'pokemon'
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'