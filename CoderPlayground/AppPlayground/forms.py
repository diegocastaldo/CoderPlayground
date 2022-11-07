from django import forms
from .models import Escritorio


class FormEscritorio(forms.Form):
    modelo=forms.CharField(max_length=40)
    medida=forms.IntegerField()
    stock=forms.IntegerField()
    
class FormMesaluz(forms.Form):
    modelo=forms.CharField(max_length=40)
    medida=forms.IntegerField()
    stock=forms.IntegerField()

class FormCajonera(forms.Form):
    modelo=forms.CharField(max_length=40)
    medida=forms.IntegerField()
    stock=forms.IntegerField()