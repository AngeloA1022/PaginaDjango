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
def pokemon_listado(request):
    if request.method == 'GET':
        pokemones = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pokemon_detalle(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)