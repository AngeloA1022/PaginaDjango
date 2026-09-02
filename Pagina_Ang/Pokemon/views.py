from django.shortcuts import render
from django.http import HttpResponse
from Pokemon import models as datos

# Create your views here.


def inicio(request):
    return render(request,'Pokemon/inicio.html')




def pokemon(request):
    data = {
        'pokemon': datos.pokemon,
    }
    return render(request,'Pokemon/pokemon.html',data)