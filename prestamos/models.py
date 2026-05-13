"""Modelo de préstamos y validaciones de negocio."""

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Prestamo(models.Model):
    """Representa el préstamo de un libro a un usuario."""

    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    libro = models.ForeignKey('libros.Libro', on_delete=models.PROTECT)
    fecha_prestamo = models.DateField(default=timezone.now)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.libro}"

    def clean(self):
        """Valida reglas de negocio antes de guardar el préstamo."""

        # Evita que la fecha de devolución sea anterior a la de préstamo.
        if self.fecha_devolucion and self.fecha_prestamo:
            if self.fecha_devolucion < self.fecha_prestamo:
                raise ValidationError({
                    'fecha_devolucion': 'La fecha de devolución no puede ser anterior al préstamo.'
                })

        # Impide prestar el mismo libro si ya existe un préstamo activo.
        if self.libro_id and not self.devuelto:
            ya_prestado = Prestamo.objects.filter(
                libro_id=self.libro_id,
                devuelto=False,
            ).exclude(pk=self.pk).exists()
            if ya_prestado:
                raise ValidationError({
                    'libro': 'Este libro ya está prestado actualmente.'
                })

    def save(self, *args, **kwargs):
        """Ejecuta validaciones completas antes de persistir el registro."""

        self.full_clean()
        super().save(*args, **kwargs)
