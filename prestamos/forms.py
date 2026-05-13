"""Formulario HTML para préstamos."""

from django import forms
from .models import Prestamo


# Formulario de préstamos para las vistas HTML.
class PrestamoForm(forms.ModelForm):
    """Permite crear y editar préstamos desde plantillas."""

    class Meta:
        model = Prestamo
        fields = ['usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'devuelto']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }
