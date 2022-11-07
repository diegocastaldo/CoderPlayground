"""CoderPlayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppPlayground.views import inicio, hijo, padre, formEscritorio, formMesaluz, formCajonera, mostrarEscritorios, mostrarMesaluz, mostrarCajonera





urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppPlayground/', include('AppPlayground.urls')),
    path('', inicio),
    path('Hijo/', hijo),
    path('Padre/', padre),
    path('FormEscritorio/', formEscritorio, name="FormEscritorio"),
    path('FormMesaluz/', formMesaluz, name="FormMesaluz"),
    path('FormCajonera/', formCajonera, name="FormCajonera"),
    path('MostrarEscritorios/', mostrarEscritorios, name="MostrarEscritorios"),
    path('MostrarMesaluz/', mostrarMesaluz, name="MostrarMesaluz"),
    path('MostrarCajonera/', mostrarCajonera, name="MostrarCajonera"),
    
]
    