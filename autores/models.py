"""Modelos relacionados con autores."""

from django.db import models


# Modelo de autores de la biblioteca.
class Autor(models.Model):
    primer_nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido}"
