from django.contrib import admin
from .models import Gestor, EstudiantePrimaria, EstudianteSecundaria

# Register your models here.

admin.site.register(Gestor)
admin.site.register(EstudiantePrimaria)
admin.site.register(EstudianteSecundaria)