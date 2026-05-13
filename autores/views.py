"""Vistas de la API REST para autores."""

from rest_framework import viewsets

from .models import Autor
from .serializers import AutorSerializer


# CRUD completo de autores para la API REST.
class AutorViewSet(viewsets.ModelViewSet):
    """Expone operaciones CRUD sobre autores."""

    queryset = Autor.objects.all().order_by('apellido', 'primer_nombre')
    serializer_class = AutorSerializer
