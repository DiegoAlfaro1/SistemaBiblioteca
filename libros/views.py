"""Vistas de la API REST para libros."""

from rest_framework import viewsets

from .models import Libro
from .serializers import LibroSerializer


# CRUD completo de libros para la API REST.
class LibroViewSet(viewsets.ModelViewSet):
    """Expone operaciones CRUD sobre libros."""

    queryset = Libro.objects.all().order_by('titulo', 'fecha_publicado')
    serializer_class = LibroSerializer
