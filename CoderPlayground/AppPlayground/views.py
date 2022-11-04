from django.shortcuts import render
from AppPlayground.forms import NobelFormulario

# Create your views here.
def inicio(request):
    return render(request,'AppPlayground/TInicio.html')

def hijo(request):
    return render(request,'AppPlayground/Hijo.html')

def padre(request):
    return render(request,'AppPlayground/Padre.html')


 
def nobelFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = NobelFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  Nobel = Nobel(nombre=informacion["nombre"], apellido=informacion["apellido"], ano=informacion["año"], especialidad=informacion["especialidad"])
                  Nobel.save()
                  return render(request, "AppPlayground/TInicio.html")
      else:
            miFormulario = NobelFormulario()
 
      return render(request, "AppPlayground/NobelFormulario.html", {"miFormulario": miFormulario})
