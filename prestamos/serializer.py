from rest_framework import serializers
from .models import Prestamo


# Serializador para exponer préstamos vía API REST.
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
