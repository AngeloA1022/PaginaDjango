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
    path('pokemon/<int:pk>/editar/', views.modificar_pokemon, name='modificarPokemon'),
    path('pokemon/<int:pk>/eliminar/', views.eliminar_pokemon, name='eliminarPokemon'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
