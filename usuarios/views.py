from rest_framework import viewsets
from .models import Usuario
from .serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('nombre_usuario')
    serializer_class = UsuarioSerializer
