from django.urls import path
from django.contrib import admin
from AppPlayground import views
from .views import *


urlpatterns = [
    path('', inicio),
    path('Padre/', padre),
    path('FormEscritorio/', formEscritorio, name="FormEscritorio"),
    path('FormMesaluz/', formMesaluz, name="FormMesaluz"),
    path('FormCajonera/', formCajonera, name="FormCajonera"),
    path('MostrarEscritorio/', mostrarEscritorio, name="MostrarEscritorio"),
    path('EliminarEscritorio/<int:id>', eliminarEscritorio, name="EliminarEscritorio"),
    path('BuscarEscritorio/', buscarEscritorio, name="BuscarEscritorio"),
    path('MostrarCajonera/', mostrarCajonera, name="MostrarCajonera"),
    path('EliminarCajonera/<int:id>', eliminarCajonera, name="EliminarCajonera"),
    path('BuscarCajonera/', buscarCajonera, name="BuscarCajonera"),
    path('MostrarMesaluz/', mostrarMesaluz, name="MostrarMesaluz"),
    path('EliminarMesaluz/<int:id>', eliminarMesaluz, name="EliminarMesaluz"),
    path('BuscarMesaluz/', buscarMesaluz, name="BuscarMesaluz"),
    path("Buscar/",buscar, name="Buscar"),
    path('listaJugador', JugadorList.as_view(), name="ListaJugador"),
    path('detalleJugador/<pk>', JugadorDetail.as_view(), name="DetalleJugador"),
    path('creaJugador/', JugadorCreate.as_view(), name="CreaJugador"),
    path('actualizaJugador/<pk>', JugadorUpdate.as_view(), name="ActualizaJugador"),
    path('eliminaJugador/<pk>', JugadorDelete.as_view(), name="EliminaJugador"),
]
