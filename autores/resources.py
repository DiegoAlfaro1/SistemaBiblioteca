"""Recursos para importar y exportar autores desde el admin."""

from import_export import resources

from .models import Autor


class AutorResource(resources.ModelResource):
    """Define los campos disponibles para Autor."""

    class Meta:
        model = Autor
        fields = ('id', 'primer_nombre', 'apellido')
        export_order = fields
