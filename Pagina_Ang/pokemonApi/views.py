from django.shortcuts import render
from Pokemon.models import Pokemon
from django.http import JsonResponse
from pokemonApi.serializers import PokemonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def pokemonesApi(request):
    Pokemones = Pokemon.objects.all()
    data = {
        'pokemones': list(
            Pokemones.values('id', 'Nombre', 'Tipo','Descripcion' ,'Imagen')
            )
    }
    return JsonResponse(data)


@api_view(['GET','POST'])
def pokemon_listado

