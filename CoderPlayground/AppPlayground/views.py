from django.shortcuts import render
from AppPlayground.forms import FormCajonera, FormEscritorio, FormMesaluz

# Create your views here.
def inicio(request):
    return render(request,'AppPlayground/TInicio.html')

def hijo(request):
    return render(request,'AppPlayground/Hijo.html')

def padre(request):
    return render(request,'AppPlayground/Padre.html')

 
def FormEscritorio(request):
 
      if request.method == "POST":
 
            miFormulario = FormEscritorio(request.POST) # Aqui me llega la informacion del html
           
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  Escritorio = Escritorio(modelo=informacion["modelo"], medida=informacion["medida"], stock=informacion["stock"])
                  Escritorio.save()
                  return render(request, "AppPlayground/TInicio.html")
      else:
            miFormulario = FormEscritorio()
 
      return render(request, "AppPlayground/FormEscritorio.html", {"miFormulario": miFormulario})
