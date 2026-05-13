from django.db import models

# Create your models here.
class Libro(models.Model):
    autor = models.ForeignKey('autores.Autor', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    fecha_publicado = models.DateField()
