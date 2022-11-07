from django.shortcuts import render
from django.template import Context, Template
from AppPlayground.forms import FormCajonera, FormEscritorio, FormMesaluz
from AppPlayground.models import Escritorio, Mesaluz, Cajonera
from django.http import HttpResponseRedirect
# Create your views here.

def inicio(request):
    return render(request,'AppPlayground/TInicio.html')

def hijo(request):
    return render(request,'AppPlayground/Hijo.html')

def padre(request):
    return render(request,'AppPlayground/Padre.html')

 
def formEscritorio(request):
 
      if request.method == 'POST':
 
            miFormulario = FormEscritorio(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  escritorio = Escritorio(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  escritorio.save()
                  return HttpResponseRedirect("/MostrarEscritorios/")
      else:
        
        miFormulario = FormEscritorio()
        
        return render(request, "AppPlayground/FormEscritorio.html", {"miFormulario": miFormulario})

def mostrarEscritorios(request):

    escritorios = Escritorio.objects.all()

    return render(request, "AppPlayground/MostrarEscritorios.html", {"escritorios": escritorios})





def formMesaluz(request):
 
      if request.method == 'POST':
 
            miFormulario = FormMesaluz(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  mesaluz = Mesaluz(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  mesaluz.save()
                  return HttpResponseRedirect("")
      else:
        
        miFormulario = FormMesaluz()
        
        return render(request, "AppPlayground/FormMesaluz.html", {"miFormulario": miFormulario})

def mostrarMesaluz(request):

    mesaluz = Mesaluz.objects.all()

    return render(request, "AppPlayground/MostrarMesaluz.html", {"mesaluz": mesaluz})





def formCajonera(request):
 
      if request.method == 'POST':
 
            miFormulario = FormCajonera(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid():
                  data = miFormulario.cleaned_data   
                  mesaluz = Cajonera(modelo=data["modelo"], medida=data["medida"], stock=data["stock"])
                  mesaluz.save()
                  return HttpResponseRedirect("")
      else:
        
        miFormulario = FormCajonera()
        
        return render(request, "AppPlayground/FormCajonera.html", {"miFormulario": miFormulario})

def mostrarCajonera(request):

    cajonera = Cajonera.objects.all()

    return render(request, "AppPlayground/MostrarCajonera.html", {"cajonera": cajonera})









    