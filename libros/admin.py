from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicado')
    search_fields = ('titulo',)
    list_filter = ('fecha_publicado',)
