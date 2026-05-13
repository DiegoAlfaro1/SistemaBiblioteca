"""Serializadores para la API REST de usuarios."""

from rest_framework import serializers

from .models import Usuario


# Serializador para exponer usuarios vía API REST.
class UsuarioSerializer(serializers.ModelSerializer):
    """Convierte usuarios a y desde JSON."""

    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuario', 'nombre']
