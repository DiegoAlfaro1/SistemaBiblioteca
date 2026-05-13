from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=30, default='default_user')