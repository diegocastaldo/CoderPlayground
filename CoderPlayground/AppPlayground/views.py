from django.shortcuts import render
from django.template import Context, Template
from AppPlayground.forms import FormCajonera, FormEscritorio, FormMesaluz
from AppPlayground.models import Escritorio, Mesaluz, Cajonera
from django.http import HttpResponseRedirect, HttpResponse
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

    return render(request, "AppPlayground/MostrarMesaluz.html", {"mesaluz": mesas})


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

    cajoneras = Escritorio.objects.all()

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





