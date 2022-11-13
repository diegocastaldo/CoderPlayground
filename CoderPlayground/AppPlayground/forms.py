from django import forms
from .models import *
#ACA VAN LOS FORMS DE LA APP DE GOLF


class FormJugador(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    nacimiento=forms.CharField()
    dni=forms.IntegerField()
    telefono=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=60)

class FormClub(forms.Form): 
    nombre=forms.CharField(max_length=30) #Nombre del Club
    par=forms.IntegerField()
    provincia=forms.CharField(max_length=30)
    telefono=forms.CharField(max_length=30)
    domicilio=forms.CharField(max_length=100)

class FormTarjeta(forms.Form):
    nombre=forms.CharField(max_length=50) #Nombre del Jugador
    score=forms.IntegerField()
    marcador=forms.CharField(max_length=50)
    club=forms.CharField()
    fecha=forms.DateField()
    s1=forms.IntegerField()
    s2=forms.IntegerField()
    s3=forms.IntegerField()
    s4=forms.IntegerField()
    s5=forms.IntegerField()
    s6=forms.IntegerField()
    s7=forms.IntegerField()
    s8=forms.IntegerField()
    s9=forms.IntegerField()
    s10=forms.IntegerField()
    s11=forms.IntegerField()
    s12=forms.IntegerField()
    s13=forms.IntegerField()
    s14=forms.IntegerField()
    s15=forms.IntegerField()
    s16=forms.IntegerField()
    s17=forms.IntegerField()
    s18=forms.IntegerField()

