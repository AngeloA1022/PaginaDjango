from django.shortcuts import render
from django.http import HttpResponse
from Pokemon.forms import PokemonForm
from Pokemon.models import Pokemon

# Create your views here.


def inicio(request):
    pokemon_list = Pokemon.objects.all()
    data = {
        'pokemon': pokemon_list,
    }
    return render(request, 'Pokemon/inicio.html', data)


def inicioadmin(request):
    return render(request, 'Pokemon/inicioadmin.html') 

#------ Pokemones ------
#
def agregar_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'Pokemon/pokemon.html', {'mensaje': 'Pokémon agregado correctamente.'})
    else:
        form = PokemonForm()
    return render(request, 'Pokemon/agregar_pokemon.html', {'form': form})   


def pokemon(request):
    pokemon_list = Pokemon.objects.all()
    data = {
        'pokemon': pokemon_list,
    }
    return render(request, 'Pokemon/pokemon.html', data)