from django.db import models

# Create your models here.
pokemon = [
    {'Nombre':'Pikachu','Tipo':'Electrico','Imagen':'pikachu.png'},
    {'Nombre':'Charizard','Tipo':'Fuego','Imagen':'charizard.png'},
    {'Nombre':'Venusaur','Tipo':'Planta','Imagen':'venusaur.png'},
    {'Nombre':'Blastoise','Tipo':'Agua','Imagen':'blastoise.png'},
    {'Nombre':'Greninja','Tipo':'Agua','Imagen':'greninja.png'},
    {'Nombre':'Decidueye','Tipo':'Planta','Imagen':'decidueye.png'},
]



class Pokemon(models.Model):
    Nombre = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Descripcion = models.TextField(max_length=500)
    Imagen = models.ImageField(upload_to='pokemon_images/')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'pokemon'
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'