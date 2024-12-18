from django.db import models

# Create your models here.

class estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    grado = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
