from django.db import models


# Modelo de usuarios de la biblioteca.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=30, default='default_user')

    def __str__(self):
        return self.nombre_usuario
