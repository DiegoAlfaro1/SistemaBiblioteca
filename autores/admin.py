from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Autor
from .resources import AutorResource


@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    # Permite importar y exportar autores desde el admin.
    resource_class = AutorResource
    list_display = ('primer_nombre', 'apellido')
    search_fields = ('primer_nombre', 'apellido')
    list_filter = ('apellido',)
