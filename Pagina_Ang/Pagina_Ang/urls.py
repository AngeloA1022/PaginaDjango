from django.contrib import admin
from django.urls import path
from Pokemon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('inicioadmin/', views.inicioadmin, name='inicioadmin'),
    path('agregar_pokemon/', views.pokemon, name='agregar_pokemon'),
]