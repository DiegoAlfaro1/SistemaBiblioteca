"""Vistas de la API REST para usuarios."""

from rest_framework import viewsets

from .models import Usuario
from .serializer import UsuarioSerializer


# CRUD completo de usuarios para la API REST.
class UsuarioViewSet(viewsets.ModelViewSet):
    """Expone operaciones CRUD sobre usuarios."""

    queryset = Usuario.objects.all().order_by('nombre_usuario')
    serializer_class = UsuarioSerializer
