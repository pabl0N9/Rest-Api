from rest_framework import serializers
from .models import EstudiantePrimaria, EstudianteSecundaria

class EstudiantePrimariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstudiantePrimaria
        fields = '__all__'

class EstudianteSecundariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstudianteSecundaria
        fields= '__all__'