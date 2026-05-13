"""Serializadores para la API REST de préstamos."""

from rest_framework import serializers
from .models import Prestamo


# Serializador para exponer préstamos vía API REST.
class PrestamoSerializer(serializers.ModelSerializer):
    """Convierte préstamos a y desde JSON."""

    class Meta:
        model = Prestamo
        fields = '__all__'
