from django.shortcuts import render
from Pokemon.models import Pokemon
from django.http import JsonResponse
from pokemonApi.serializers import PokemonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import DatabaseError, OperationalError
from Pagina_Ang.datos_offline import guardar_datos_offline


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
            try:
                pokemon = serializer.save()
                return Response(PokemonSerializer(pokemon).data, status=status.HTTP_201_CREATED)
            except (DatabaseError, OperationalError):
                guardar_datos_offline("crear", dict(serializer.validated_data))
                return Response(
                    {"detail": "Información guardada en datos_offline"},
                    status=status.HTTP_202_ACCEPTED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pokemon_detalle(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except (DatabaseError, OperationalError):
        if request.method == 'PUT':
            serializer = PokemonSerializer(data=request.data)
            if serializer.is_valid():
                guardar_datos_offline("editar", dict(serializer.validated_data), pk)
                return Response(
                    {"detail": "Información guardada en datos_offline"},
                    status=status.HTTP_202_ACCEPTED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            guardar_datos_offline("eliminar", {}, pk)
            return Response(
                {"detail": "Información guardada en datos_offline"},
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            try:
                pokemon = serializer.save()
                return Response(PokemonSerializer(pokemon).data)
            except (DatabaseError, OperationalError):
                guardar_datos_offline("editar", dict(serializer.validated_data), pk)
                return Response(
                    {"detail": "Información guardada en datos_offline"},
                    status=status.HTTP_202_ACCEPTED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            pokemon.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (DatabaseError, OperationalError):
            guardar_datos_offline("eliminar", {}, pk)
            return Response(
                {"detail": "Información guardada en datos_offline"},
                status=status.HTTP_202_ACCEPTED,
            )