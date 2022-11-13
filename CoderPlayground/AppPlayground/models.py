from django.db import models

# Create your models here.
class Escritorio(models.Model):
    modelo=models.CharField(max_length=50)
    medida=models.IntegerField()
    stock=models.IntegerField()

    def __str__(self):
        return f'{self.modelo} - {self.medida}'

class Mesaluz(models.Model):
    modelo=models.CharField(max_length=50)
    medida=models.IntegerField()
    stock=models.IntegerField()

    def __str__(self):
            return f'{self.modelo} - {self.medida}'

class Cajonera(models.Model):
    modelo=models.CharField(max_length=50)
    medida=models.IntegerField()
    stock=models.IntegerField()
    
    def __str__(self):
            return f'{self.modelo} - {self.medida}'

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

