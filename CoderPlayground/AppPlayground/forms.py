from django import forms

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
    cajones=forms.IntegerField()
    stock=forms.IntegerField()
