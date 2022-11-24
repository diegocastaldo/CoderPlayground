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
    marcador=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    fecha=models.DateField(default=0)
    s1=models.IntegerField(default=0)
    s2=models.IntegerField(default=0)
    s3=models.IntegerField(default=0)
    s4=models.IntegerField(default=0)
    s5=models.IntegerField(default=0)
    s6=models.IntegerField(default=0)
    s7=models.IntegerField(default=0)
    s8=models.IntegerField(default=0)
    s9=models.IntegerField(default=0)
    s10=models.IntegerField(default=0)
    s11=models.IntegerField(default=0)
    s12=models.IntegerField(default=0)
    s13=models.IntegerField(default=0)
    s14=models.IntegerField(default=0)
    s15=models.IntegerField(default=0)
    s16=models.IntegerField(default=0)
    s17=models.IntegerField(default=0)
    s18=models.IntegerField(default=0)


    
    def __str__(self):
            return f'{self.club}'

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
