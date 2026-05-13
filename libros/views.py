from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo', 'fecha_publicado')
    serializer_class = LibroSerializer
