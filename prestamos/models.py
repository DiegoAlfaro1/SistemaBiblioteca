from tkinter.constants import CASCADE

from django.db import models

# Create your models here.
class Prestamo(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    libro = models.ForeignKey('libros.Libro', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
