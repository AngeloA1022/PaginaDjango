import os
from django.conf import settings
from django.shortcuts import redirect, render
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
def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            pokemon = form.save(commit=False)

            archivo = request.FILES.get('Imagen')
            if archivo:
                nombre_archivo = archivo.name
                carpeta = os.path.join(settings.MEDIA_ROOT, 'images')
                os.makedirs(carpeta, exist_ok=True)

                ruta = os.path.join(carpeta, nombre_archivo)
                with open(ruta, 'wb+') as destino:
                    for chunk in archivo.chunks():
                        destino.write(chunk)

                pokemon.Imagen = nombre_archivo

            pokemon.save()
            return redirect('pokemon')
    else:
        form = PokemonForm()
    return render(request, 'Pokemon/pokemonAdd.html', {'form': form})   


def pokemon(request):
    pokemon_list = Pokemon.objects.all()
    data = {
        'pokemon': pokemon_list,
    }
    return render(request, 'Pokemon/pokemon.html', data)

def todos_pokemon(request):
    pokemones = Pokemon.objects.all()

    data = {
        'pokemones': pokemones
    }
    return render(request, 'Pokemon/pokemon.html', data)