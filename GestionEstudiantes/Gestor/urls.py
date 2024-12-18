from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'EstudiantesPrimaria', views.EstudiantePrimariaViewSets, basename='primaria')
router.register(r'EstudiantesSecundaria', views.EstudianteSecundariaViewSets, basename='secundaria')

urlpatterns = [
    path('', views.home, name='Index'),
    path('editarEstudianteSecundaria/', views.editarEstudianteSecundaria),
    path('estudiantesPrimaria/', views.estudiantePrimaria, name='Primaria'),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('edicionEstudiante/<id_estudiante>', views.edicionEstudiante, name='edicionEstudiante'),
    path('editarEstudiante/', views.editarEstudiante),
    path('eliminarEstudiante/<id_estudiante>', views.eliminarEstudiante, name='eliminarEstudiante'),
    path('registrarEstudiantePrimaria/', views.registrarEstudiantePrimaria),
    path('estudianteSecundaria/', views.estudianteSecundaria, name='Secundaria'),
    path('registrarEstudianteSecundaria/', views.registrarEstudianteSecundaria, name='RegistrarSecundaria'),
    path('edicionEstudianteSecundaria/<id_estudiante>', views.edicionEstudianteSecundaria, name='edicionSecundaria'),
    path('eliminarEstudianteSecundaria/<id_estudiante>', views.eliminarEstudianteSecundaria, name='eliminarEstudianteSecundaria'),

    # API 
    path('api/v1/', include(router.urls))
]