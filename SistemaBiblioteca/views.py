"""
Vistas auxiliares del proyecto SistemaBiblioteca.

Se usan para respuestas compartidas como la página 404 personalizada.
"""

from django.shortcuts import render


def pagina_no_encontrada(request, exception):
    """Renderiza una página 404 personalizada en español."""
    return render(request, '404.html', status=404)
