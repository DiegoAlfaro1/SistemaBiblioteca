from django.contrib import admin
from .models import Prestamo


# Configuración del modelo Prestamo en el panel de administración.
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_prestamo')
    search_fields = ('fecha_prestamo',)

