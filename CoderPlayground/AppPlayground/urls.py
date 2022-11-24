from django.urls import path
from django.contrib import admin
from AppPlayground import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Inicio', inicio, name="Inicio"),
    path('listaJugador', JugadorList.as_view(), name="ListaJugador"),
    path('detalleJugador/<pk>', JugadorDetail.as_view(), name="DetalleJugador"),
    path('creaJugador/', JugadorCreate.as_view(), name="CreaJugador"),
    path('actualizaJugador/<pk>', JugadorUpdate.as_view(), name="ActualizaJugador"),
    path('eliminaJugador/<pk>', JugadorDelete.as_view(), name="EliminaJugador"),
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
    path('listaTarjeta', TarjetaList.as_view(), name="ListaTarjeta"),
    path('detalleTarjeta/<pk>', TarjetaDetail.as_view(), name="DetalleTarjeta"),
    path('creaTarjeta/', TarjetaCreate.as_view(), name="CreaTarjeta"),
    path('actualizaTarjeta/<pk>', TarjetaUpdate.as_view(), name="ActualizaTarjeta"),
    path('eliminaTarjeta/<pk>',TarjetaDelete.as_view(), name="EliminaTarjeta"),
]
