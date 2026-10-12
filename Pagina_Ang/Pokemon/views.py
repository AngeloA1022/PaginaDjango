import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from Pokemon.forms import PokemonForm
from Pokemon.models import Pokemon

# Create your views here.


def normalizar_imagenes():
    for pokemon in Pokemon.objects.all():
        if not pokemon.Imagen:
            continue

        valor = pokemon.Imagen.strip().replace('\\', '/')
        nombre = os.path.basename(valor)

        static_path = os.path.join(settings.BASE_DIR, 'static', 'images', nombre)
        media_path = os.path.join(settings.MEDIA_ROOT, 'images', nombre)
        media_root_path = os.path.join(settings.MEDIA_ROOT, nombre)

        if os.path.exists(static_path):
            pokemon.Imagen = nombre
            pokemon.save(update_fields=['Imagen'])
        elif os.path.exists(media_path):
            pokemon.Imagen = f"images/{nombre}"
            pokemon.save(update_fields=['Imagen'])
        elif os.path.exists(media_root_path):
            pokemon.Imagen = nombre
            pokemon.save(update_fields=['Imagen'])


def inicio(request):
    normalizar_imagenes()
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
                pokemon.Imagen = default_storage.save(
                    f'images/{archivo.name}',
                    archivo,
                )

            pokemon.save()
            return redirect('pokemones')
    else:
        form = PokemonForm()
    return render(request, 'Pokemon/pokemonAdd.html', {
        'form': form,
        'accion': 'Agregar Pokémon',
        'boton': 'Guardar',
    })


#Cargar pokemones para modificar
def cargar_editar_pokemon(request,pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    form = PokemonForm(instance=pokemon)

    return render(request, 'Pokemon/pokemonEdit.html', {'form': form, 'pokemon': pokemon})

def editar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save(commit=False)
            archivo = request.FILES.get('Imagen')
            if archivo:
                pokemon.Imagen = default_storage.save(
                    f'images/{archivo.name}',
                    archivo,
                )
            pokemon.save()
            return redirect('pokemones')
    
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, 'Pokemon/pokemonEdit.html', {'form': form, 'pokemon': pokemon})


def eliminar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokemones')
    return render(request, 'Pokemon/pokemonDel.html', {'pokemon': pokemon})


def pokemon(request):
    return redirect('pokemones')

def todos_pokemon(request):
    normalizar_imagenes()
    pokemones = Pokemon.objects.all()

    data = {
        'pokemones': pokemones
    }
    return render(request, 'Pokemon/pokemon.html', data)