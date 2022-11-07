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

class Cajonera(models.Model):
    modelo=models.CharField(max_length=50)
    medida=models.IntegerField()
    stock=models.IntegerField()
    cajones=models.IntegerField()