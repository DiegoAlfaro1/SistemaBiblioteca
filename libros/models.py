"""Modelos relacionados con libros."""

from django.db import models


# Modelo de libros de la biblioteca.
class Libro(models.Model):
    autor = models.ForeignKey('autores.Autor', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    fecha_publicado = models.DateField()

    def __str__(self):
        return self.titulo
