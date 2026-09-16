from django.contrib import admin
from Pokemon.models import Pokemon

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Tipo', 'Descripcion', 'Imagen']


admin.site.register(Pokemon, PokemonAdmin)