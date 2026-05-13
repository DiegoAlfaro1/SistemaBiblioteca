from django.contrib import admin
from .models import Usuario


# Configuración del modelo Usuario en el panel de administración.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombe_usuario',)

