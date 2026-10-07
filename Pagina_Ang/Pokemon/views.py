import os
from django.conf import settings
from django.shortcuts import redirect, render
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
                nombre_archivo = archivo.name
                carpeta = os.path.join(settings.MEDIA_ROOT, 'images')
                os.makedirs(carpeta, exist_ok=True)

                ruta = os.path.join(carpeta, nombre_archivo)
                with open(ruta, 'wb+') as destino:
                    for chunk in archivo.chunks():
                        destino.write(chunk)

                pokemon.Imagen = f"images/{nombre_archivo}"

            pokemon.save()
            return redirect('pokemones')
    else:
        form = PokemonForm()
    return render(request, 'Pokemon/pokemonAdd.html', {'form': form})   


def pokemon(request):
    return redirect('pokemones')

def todos_pokemon(request):
    normalizar_imagenes()
    pokemones = Pokemon.objects.all()

    data = {
        'pokemones': pokemones
    }
    return render(request, 'Pokemon/pokemones.html', data)