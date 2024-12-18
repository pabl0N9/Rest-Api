from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Gestor(models.Model):
    id_estudiante = models.IntegerField(null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)

    def MostrarInfo(self):
        return f"Documento: {self.id_estudiante}", "Nombre: {self.nombre}", "Apellido: {self.apellido}"
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre, self.apellido)

class EstudiantePrimaria(Gestor):
    grado = models.IntegerField(null=False)
# este mostrar info se utiliza en views.py y muestra la informacion de los estudiantes de primaria
    def MostrarInfo(self):
        if self == None:
            return False
        else:
            for self in self:
                
                return f"Documento: {self.id_estudiante} Nombre: {self.nombre} Grado: {self.grado}"

class EstudianteSecundaria(Gestor):
    _especialidad = models.CharField(max_length=50)

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, value):
        self._especialidad = value

#  este mostrar info se utiliza en views.py y muestra la informacion de los estudiantes de secundaria
    def MostrarInfo(self):
        if self == None:
            return False
        else:
            for self in self:
                return f"Documento: {self.id_estudiante} Nombre: {self.nombre} Especialidad: {self._especialidad}"