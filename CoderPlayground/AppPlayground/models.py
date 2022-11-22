from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Jugador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    nacimiento=models.CharField(max_length=30)
    dni=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    def __str__(self):
            return f'{self.apellido} , {self.nombre}'

class Club(models.Model): 
    nombre=models.CharField(max_length=30) #Nombre del Club
    par=models.IntegerField()
    provincia=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    domicilio=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    def __str__(self):
            return f'Club "{self.nombre}" , provincia de  {self.provincia}.'

class Tarjeta(models.Model):
    nombre=models.CharField(max_length=50) #Nombre del Jugador
    score=models.IntegerField()
    marcador=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    fecha=models.DateField()
    
    def __str__(self):
            return f'{self.club} , {self.score}'

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
