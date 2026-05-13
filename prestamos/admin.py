from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Prestamo
from .resources import PrestamoResource


@admin.register(Prestamo)
class PrestamoAdmin(ImportExportModelAdmin):
    # Permite importar y exportar préstamos desde el admin.
    resource_class = PrestamoResource
    list_display = ('usuario', 'fecha_prestamo')
    search_fields = ('fecha_prestamo',)

