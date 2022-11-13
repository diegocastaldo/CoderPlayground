from django.shortcuts import render
from django.template import Context, Template
from AppPlayground.forms import FormCajonera, FormEscritorio, FormMesaluz, FormJugador, FormClub, FormTarjeta
from AppPlayground.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
# Create your views here.

def inicio(request):
    return render(request,'AppPlayground/TInicio.html')

def hijo(request):
    return render(request,'AppPlayground/Hijo.html')

def padre(request):
    return render(request,'AppPlayground/Padre.html')

#ACA VAN LAS FUNCIONES DE ESCRITORIOS#
 
def formEscritorio(request):
 
      if request.method == 'POST':
 
            miFormulario = FormEscritorio(request.POST) 
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  escritorio = Escritorio(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  escritorio.save()
                  return HttpResponseRedirect("AppPlayground/MostrarEscritorio/")
      else:
        
        miFormulario = FormEscritorio()
        
        return render(request, "AppPlayground/FormEscritorio.html", {"miFormulario": miFormulario})

def mostrarEscritorio(request):

    escritorios = Escritorio.objects.all()

    return render(request, "AppPlayground/MostrarEscritorio.html", {"escritorios": escritorios})


def eliminarEscritorio(request, id):

    if request.method == 'POST':

        escritorio = Escritorio.objects.get(id=id)
        escritorio.delete()

        escritorios = Escritorio.objects.all()

        return render(request, "AppPlayground/MostrarEscritorio.html", {"escritorios": escritorios})        



def buscarEscritorio(request):
    return render(request, "AppPlayground/BuscarEscritorio.html")

def buscar(request):
 

    if request.GET["modelo"]:

        modelo = request.GET["modelo"]

        escritorios = Escritorio.objects.filter(modelo__icontains=modelo)
        
        return render(request, "AppPlayground/ResultEscritorio.html", {"escritorios": escritorios, "modelo": modelo})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

#ACA VAN LAS FUNCIONES DE MESAS DE LUZ#


def formMesaluz(request):
 
      if request.method == 'POST':
 
            miFormulario = FormMesaluz(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  mesaluz = Mesaluz(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  mesaluz.save()
                  return HttpResponseRedirect("/MostrarMesaluz/")
      else:
        
        miFormulario = FormMesaluz()
        
        return render(request, "AppPlayground/FormMesaluz.html", {"miFormulario": miFormulario})

def mostrarMesaluz(request):

    mesas = Mesaluz.objects.all()

    return render(request, "AppPlayground/MostrarMesaluz.html", {"mesas": mesas})


def eliminarMesaluz(request, id):

    if request.method == 'POST':

        mesa = Mesaluz.objects.get(id=id)
        mesa.delete()

        mesas = Mesaluz.objects.all()

        return render(request, "AppPlayground/MostrarMesaluz.html", {"mesas": mesas})        



def buscarMesaluz(request):
    return render(request, "AppPlayground/BuscarMesaluzhtml")

def buscar(request):
 

    if request.GET["modelo"]:

        modelo = request.GET["modelo"]

        mesas = Mesaluz.objects.filter(modelo__icontains=modelo)
        
        return render(request, "AppPlayground/ResultMesaluz.html", {"mesas": mesas, "modelo": modelo})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

#ACA VAN LAS FUNCIONES DE CAJONERAS#


def formCajonera(request):
 
      if request.method == 'POST':
 
            miFormulario = FormCajonera(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  mesaluz = Cajonera(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  mesaluz.save()
                  return HttpResponseRedirect("/MostrarCajonera/")
      else:
        
        miFormulario = FormCajonera()
        
        return render(request, "AppPlayground/FormCajonera.html", {"miFormulario": miFormulario})


def mostrarCajonera(request):

    cajoneras = Cajonera.objects.all()

    return render(request, "AppPlayground/MostrarCajonera.html", {"cajoneras": cajoneras})


def eliminarCajonera(request, id):

    if request.method == 'POST':

        cajonera = Cajonera.objects.get(id=id)
        cajonera.delete()

        cajoneras = Cajonera.objects.all()

        return render(request, "AppPlayground/MostrarCajonera.html", {"cajoneras": cajoneras})        



def buscarCajonera(request):
    return render(request, "AppPlayground/BuscarCajonera.html")

def buscar(request):
 

    if request.GET["modelo"]:

        modelo = request.GET["modelo"]

        cajoneras = Cajonera.objects.filter(modelo__icontains=modelo)
        
        return render(request, "AppPlayground/ResultCajonera.html", {"cajoneras": cajoneras, "modelo": modelo})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


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


