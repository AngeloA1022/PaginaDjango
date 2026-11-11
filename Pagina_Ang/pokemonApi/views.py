from django.shortcuts import render
from Pokemon.models import Pokemon
from django.http import JsonResponse


def pokemonesApi(request):
    Pokemones = Pokemon.objects.all()
    data = {
        'pokemones': list(
            Pokemones.values('id', 'Nombre', 'Tipo','Descripcion' ,'Imagen')
            )
    }
    return JsonResponse(data)

# Create your views here.
