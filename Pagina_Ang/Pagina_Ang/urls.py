from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Pokemon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('inicioadmin/', views.inicioadmin, name='inicioadmin'),
    path('pokemonAdd/', views.crear_pokemon, name='crearPokemon'),
    path('pokemones/', views.todos_pokemon, name='pokemones'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

