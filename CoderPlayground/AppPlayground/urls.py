from django.urls import path
from django.contrib import admin
from AppPlayground import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Padre/', padre, name="Padre"),
    path('listaJugador', JugadorList.as_view(), name="ListaJugador"),
    path('detalleJugador/<pk>', JugadorDetail.as_view(), name="DetalleJugador"),
    path('creaJugador/', JugadorCreate.as_view(), name="CreaJugador"),
    path('actualizaJugador/<pk>', JugadorUpdate.as_view(), name="ActualizaJugador"),
    path('eliminaJugador/<pk>', JugadorDelete.as_view(), name="EliminaJugador"),
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil")
]
