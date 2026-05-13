from rest_framework import serializers

from .models import Autor


# Serializador para exponer autores vía API REST.
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'primer_nombre', 'apellido']
