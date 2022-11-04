from socket import fromshare
from django import forms

class NobelFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    ano=forms.DateField()
    especialidad=forms.CharField(max_length=40)
    


