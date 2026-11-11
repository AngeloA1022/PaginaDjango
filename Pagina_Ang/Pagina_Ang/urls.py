from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from pokemonApi import views as vistasApi
from django.contrib import admin
from django.urls import include, path
from Pokemon import views

handler500 = 'Pagina_Ang.views.error_db_view'
handler404 = 'Pagina_Ang.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('', views.inicio, name='inicio'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('inicioadmin/', views.inicioadmin, name='inicioadmin'),
    path('pokemonAdd/', views.crear_pokemon, name='crearPokemon'),
    path('pokemones/', views.todos_pokemon, name='pokemones'),
    path('pokemonEdit/<int:pokemon_id>/', views.cargar_editar_pokemon, name='editarPokemon'),
    path('pokemonEditado/<int:pokemon_id>/', views.editar_pokemon, name='pokemonEditado'),
    path('pokemonDel/<int:pokemon_id>/', views.eliminar_pokemon, name='eliminarPokemon'),
    path('accounts/' , include('django.contrib.auth.urls')),

    # Rutas de la API
    path('pokemonesApi/', vistasApi.pokemonesApi, name='pokemonesApi'),
    path('pokemonesListApi/', vistasApi.pokemon_listado, name='pokemonesListoApi'),
    path('pokemonesListApi/<int:pk>/', vistasApi.pokemon_detalle, name='pokemonDetalleApi'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
