from django.urls import path
from django.contrib import admin
from AppPlayground import views
from .views import *


urlpatterns = [
    path('', inicio),
    path('Padre/', padre),
    path('listaJugador', JugadorList.as_view(), name="ListaJugador"),
    path('detalleJugador/<pk>', JugadorDetail.as_view(), name="DetalleJugador"),
    path('creaJugador/', JugadorCreate.as_view(), name="CreaJugador"),
    path('actualizaJugador/<pk>', JugadorUpdate.as_view(), name="ActualizaJugador"),
    path('eliminaJugador/<pk>', JugadorDelete.as_view(), name="EliminaJugador"),
]
