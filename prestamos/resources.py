"""Recursos para importar y exportar préstamos desde el admin."""

from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from libros.models import Libro
from usuarios.models import Usuario

from .models import Prestamo


class PrestamoResource(resources.ModelResource):
    """Define los campos disponibles para Prestamo."""

    # Se exportan e importan las relaciones usando ids.
    usuario = Field(
        column_name='usuario',
        attribute='usuario',
        widget=ForeignKeyWidget(Usuario, 'id'),
    )
    libro = Field(
        column_name='libro',
        attribute='libro',
        widget=ForeignKeyWidget(Libro, 'id'),
    )

    class Meta:
        model = Prestamo
        fields = ('id', 'usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'devuelto')
        export_order = fields
