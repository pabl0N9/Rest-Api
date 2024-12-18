from rest_framework import viewsets
from .serializer import estudianteSerializer
from .models import estudiante 

# Create your views here.

class estudianteViewsSet(viewsets.ModelViewSet):
    queryset = estudiante.objects.all()
    serializer_class = estudianteSerializer