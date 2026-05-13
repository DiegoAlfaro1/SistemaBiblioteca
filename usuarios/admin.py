from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import Usuario


# Configuración del modelo Usuario en el panel de administración.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_usuario')
    search_fields = ('nombre_usuario', 'nombre')


# Los grupos de Django se usan como roles simples dentro del panel de administración.
admin.site.unregister(Group)


@admin.register(Group)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('permissions',)


# El modelo Permission permite asignar permisos granulares a usuarios o grupos.
@admin.register(Permission)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'codename')
    list_filter = ('content_type',)

