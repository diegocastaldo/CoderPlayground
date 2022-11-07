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
                  return HttpResponseRedirect("")
      else:
        
        miFormulario = FormEscritorio()
        
        return render(request, "AppPlayground/FormEscritorio.html", {"miFormulario": miFormulario})

def mostrarEscritorios(request):

    escritorios = Escritorio.objects.all()

    return render(request, "AppPlayground/MostrarEscritorios.html", {"escritorios": escritorios})

