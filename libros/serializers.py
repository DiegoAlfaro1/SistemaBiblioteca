"""Serializadores para la API REST de libros."""

from rest_framework import serializers

from .models import Libro


# Serializador para exponer libros vía API REST.
class LibroSerializer(serializers.ModelSerializer):
    """Convierte libros a y desde JSON."""

    class Meta:
        model = Libro
        fields = ['id', 'autor', 'titulo', 'fecha_publicado']
