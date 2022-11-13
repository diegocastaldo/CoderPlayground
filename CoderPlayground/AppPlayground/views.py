from django.shortcuts import render
from django.template import Context, Template
from AppPlayground.forms import FormCajonera, FormEscritorio, FormMesaluz, FormJugador, FormClub, FormTarjeta
from AppPlayground.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
# Create your views here.

# VIEWS DE JUGADOR
class JugadorList(ListView):

    model = Jugador
    template_name = 'jugador_list.html'
    context_object_name = "jugadores"

class JugadorDetail(DetailView):

    model = Jugador
    template_name = 'AppPlayground/jugador_detail.html'
    context_object_name = "jugador"

class JugadorCreate(CreateView):

    model = Jugador
    template_name = 'AppPlayground/jugador_create.html'
    fields = ["nombre", "apellido", "nacimiento", "dni", "telefono", "email"]
    success_url = '/AppGolf/listaJugador'


class JugadorUpdate(UpdateView):

    model = Jugador
    template_name = 'AppPlayground/jugador_update.html'
    fields = ('__all__')
    success_url = '/AppGolf/listaJugador'

class JugadorDelete(DeleteView):

    model = Jugador
    template_name = 'AppPlayground/jugador_delete.html'
    success_url = '/AppGolf/listaJugador'

# VIEWS DE CLUB
class ClubList(ListView):

    model = Club
    template_name = 'AppPlayground/club_list.html'
    context_object_name = "clubes"

class ClubDetail(DetailView):

    model = Club
    template_name = 'AppPlayground/club_detail.html'
    context_object_name = "club"

class ClubCreate(CreateView):

    model = Club
    template_name = 'AppPlayground/club_create.html'
    fields = ["nombre", "par", "provincia", "telefono", "domicilio", "email"]
    success_url = '/jugador_list/'


class ClubUpdate(UpdateView):

    model = Club
    template_name = 'AppPlayground/club_update.html'
    fields = ('__all__')
    success_url = '/club_list/'

class ClubDelete(DeleteView):

    model = Club
    template_name = 'AppPlayground/club_delete.html'
    success_url = '/club_list/'



# VIEWS DE TARJETAS
class TarjetaList(ListView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_list.html'
    context_object_name = "tarjetas"

class TarjetaDetail(DetailView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_detail.html'
    context_object_name = "tarjeta"

class TarjetaCreate(CreateView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_create.html'
    fields = ["club", "fecha", "s1", "s2", "s3", "s4", "s5", "s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18"]
    success_url = '/tarjeta_list/'


class TarjetaUpdate(UpdateView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_update.html'
    fields = ('__all__')
    success_url = '/tarjeta_list/'

class TarjetaDelete(DeleteView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_delete.html'
    success_url = '/tarjeta_list/'


