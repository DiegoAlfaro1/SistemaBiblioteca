from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Libro
from .resources import LibroResource


@admin.register(Libro)
class LibroAdmin(ImportExportModelAdmin):
    # Permite importar y exportar libros desde el admin.
    resource_class = LibroResource
    list_display = ('titulo', 'autor', 'fecha_publicado')
    search_fields = ('titulo',)
    list_filter = ('fecha_publicado',)
