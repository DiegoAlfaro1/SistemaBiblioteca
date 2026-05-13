"""Recursos para importar y exportar usuarios desde el admin."""

from import_export import resources

from .models import Usuario


class UsuarioResource(resources.ModelResource):
    """Define los campos disponibles para Usuario."""

    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'nombre_usuario')
        export_order = fields
