from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class nobel(models.Model):
    nomre=models.CharField(max_length=50)
    año=models.IntegerField()
    campo=models.CharField(max_length=20)

