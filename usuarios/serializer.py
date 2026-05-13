from rest_framework import serializers
from .models import Usuario


# Serializador para exponer usuarios vía API REST.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuario', 'nombre']
