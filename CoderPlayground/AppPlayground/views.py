from django.shortcuts import render
from django.template import Context, Template
from AppPlayground.forms import FormJugador, FormClub, FormTarjeta, UserCreationForm, UserEditForm, UserRegisterForm
from AppPlayground.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LogoutView
# Create your views here.

def inicio(request):
    return render(request,'AppPlayground/TInicio.html')


# ACÁ VAN LAS VIEWS DE LA APP DE GOLF 


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
    success_url = 'AppGolf/listaTarjeta/'


class TarjetaUpdate(UpdateView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_update.html'
    fields = ('__all__')
    success_url = '/listaTarjeta/'

class TarjetaDelete(DeleteView):

    model = Tarjeta
    template_name = 'AppPlayground/tarjeta_delete.html'
    success_url = '/listaTarjeta/'


#ACÁ VAN LAS VIEWS RELACIONADAS AL LOGIN Y CONTROL DE USUARIOS: 

def loginView(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "TInicio.html", {"mensaje": f'Bienvenido {usuario} a IHS' })
            
            else:

                return render(request, "TInicio.html", {"mensaje": f'Los datos ingresados no son correctos'})

        return render(request, "TInicio.html", {"mensaje": f'Error, formulario invalido'})

    else:

        miFormulario = AuthenticationForm()

        return render(request, "AppPlayground/login.html", {"miFormulario": miFormulario})


def register(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]

            miFormulario.save()

            return render(request, "AppPlayground/TInicio.html", {"mensaje": f'Usuario {username} creado con éxito'})

        else:

            return render(request, "AppPlayground/TInicio.html", {"mensaje": f'Error al crear el usuario'})

    else:

        miFormulario = UserRegisterForm()

        return render(request, "AppPlayground/registro.html", {"miFormulario": miFormulario})


def editar_perfil(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])

            usuario.save()

            return render(request, "TInicio.html", {"mensaje": f'Datos actualizados!'})
        
        return render(request, "editarPerfil.html", {"mensaje": 'Contraseñas no coinciden'} )
    
    else:

        miFormulario = UserEditForm(instance=request.user)

        return render(request, "editarPerfil.html", {"miFormulario": miFormulario})
