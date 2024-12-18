from django.shortcuts import render, redirect
from .models import Gestor, EstudiantePrimaria, EstudianteSecundaria

from rest_framework import viewsets
from .serializers import EstudiantePrimariaSerializers, EstudianteSecundariaSerializers


class EstudiantePrimariaViewSets(viewsets.ModelViewSet):
    queryset = EstudiantePrimaria.objects.all()
    serializer_class = EstudiantePrimariaSerializers

class EstudianteSecundariaViewSets(viewsets.ModelViewSet):
    queryset = EstudianteSecundaria.objects.all()
    serializer_class = EstudianteSecundariaSerializers

# Create your views here.

def home(request):
    estudiantes_primaria = EstudiantePrimaria.objects.all()
    estudiantes_secundaria = EstudianteSecundaria.objects.all()

    return render(request, "index.html", {
        "estudiantes_primaria": estudiantes_primaria,
        "estudiantes_secundaria": estudiantes_secundaria,
# Se utiliza el metodo mostrar info de las clases hijas primaria y secundaria (polimorfismo)
        "MostrarSec" : EstudianteSecundaria.MostrarInfo(estudiantes_secundaria),
        "MostrarPri" : EstudiantePrimaria.MostrarInfo(estudiantes_primaria)
        })

def registrarEstudiante(request):
    id_estudiante = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    
    estudiante = Gestor.objects.create(id_estudiante=id_estudiante, nombre=nombre, apellido=apellido)
    return redirect('/')

def edicionEstudiante(request, id_estudiante):
    estudiante = EstudiantePrimaria.objects.get(id_estudiante=id_estudiante)
    return render(request, "edicionEstudiante.html",{"estudiante": estudiante})

def editarEstudiante(request):
    id_estudiante = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    grado = request.POST['txtGrado']

    estudiante = EstudiantePrimaria.objects.get(id_estudiante=id_estudiante)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.grado = grado
    estudiante.save()

    return redirect('/')

def eliminarEstudiante(request, id_estudiante):
    estudiante = Gestor.objects.get(id_estudiante=id_estudiante)
    estudiante.delete()

    return redirect('/')

# CRUD primaria

def estudiantePrimaria(request):
    estudiantes = EstudiantePrimaria.objects.all()
    print(estudiantes)
    return render(request, "primaria.html", {"estudiantes": estudiantes})

def registrarEstudiantePrimaria(request):
    id_estudiante = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    grado = request.POST['txtGrado']

    estudiantePrimaria = EstudiantePrimaria.objects.create(id_estudiante = id_estudiante, nombre=nombre,
     apellido=apellido, grado=grado)
    return redirect('/')

# CRUD secundaria

def estudianteSecundaria(request):
    estudiantes = EstudianteSecundaria.objects.all()
    print(estudiantes)
    return render(request, "secundaria.html", {"estudiantes": estudiantes})

def registrarEstudianteSecundaria(request):
    print(request.POST)
    id_estudiante = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    especialidad = request.POST['txtEspecialidad']

    estudiantes = EstudianteSecundaria.objects.create(id_estudiante = id_estudiante, nombre=nombre,
     apellido=apellido, especialidad=especialidad)
    return redirect('/')

def edicionEstudianteSecundaria(request, id_estudiante):
    estudiante = EstudianteSecundaria.objects.get(id_estudiante=id_estudiante)
    return render(request, "edicionSecundaria.html",{"estudiante": estudiante})

def editarEstudianteSecundaria(request):
    id_estudiante = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    especialidad = request.POST['txtEspecialidad']

    estudiante = EstudianteSecundaria.objects.get(id_estudiante=id_estudiante)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.especialidad = especialidad
    estudiante.save()

    return redirect('/')

def eliminarEstudianteSecundaria(request, id_estudiante):
    estudiante = EstudianteSecundaria.objects.get(id_estudiante=id_estudiante)
    estudiante.delete()

    return redirect('/')