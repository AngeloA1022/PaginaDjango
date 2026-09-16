from django.shortcuts import render
from django.http import HttpResponse
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


def pokemon(request):
    pokemon_list = Pokemon.objects.all()
    data = {
        'pokemon': pokemon_list,
    }
    return render(request, 'Pokemon/pokemon.html', data)