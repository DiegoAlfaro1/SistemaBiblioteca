from rest_framework import viewsets

from .models import Autor
from .serializers import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('apellido', 'primer_nombre')
    serializer_class = AutorSerializer
