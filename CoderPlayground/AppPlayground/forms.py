from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
#ACA VAN LOS FORMS DE LA APP DE GOLF


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ('username', 'last_name', 'first_name', 'email')




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

