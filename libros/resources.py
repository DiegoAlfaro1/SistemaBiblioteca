"""Recursos para importar y exportar libros desde el admin."""

from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from autores.models import Autor

from .models import Libro


class LibroResource(resources.ModelResource):
    """Define los campos disponibles para Libro."""

    # Se usa el id del autor para que el admin pueda resolver la relación.
    autor = Field(
        column_name='autor',
        attribute='autor',
        widget=ForeignKeyWidget(Autor, 'id'),
    )

    class Meta:
        model = Libro
        fields = ('id', 'autor', 'titulo', 'fecha_publicado')
        export_order = fields
