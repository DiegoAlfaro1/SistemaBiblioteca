from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from import_export.admin import ImportExportModelAdmin

from .models import Usuario
from .resources import UsuarioResource


@admin.register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin):
    # Permite importar y exportar usuarios desde el admin.
    resource_class = UsuarioResource
    list_display = ('nombre', 'nombre_usuario')
    search_fields = ('nombre_usuario', 'nombre')


admin.site.unregister(Group)


@admin.register(Group)
class GrupoAdmin(admin.ModelAdmin):
    # Admin simple para administrar grupos y permisos.
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('permissions',)


@admin.register(Permission)
class PermisoAdmin(admin.ModelAdmin):
    # Admin simple para ver permisos de forma ordenada.
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'codename')
    list_filter = ('content_type',)

