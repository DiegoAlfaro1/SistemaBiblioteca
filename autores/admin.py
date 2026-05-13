from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'apellido')
    search_fields = ('primer_nombre',)
    list_filter = ('apellido',)
