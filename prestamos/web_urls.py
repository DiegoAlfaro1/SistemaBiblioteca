from django.urls import path
from .views import (
    prestamo_list,
    prestamo_create,
    prestamo_update,
    prestamo_delete,
)


# Rutas de las vistas HTML de préstamos.
urlpatterns = [
    path('prestamos/', prestamo_list, name='prestamo_list'),
    path('prestamos/nuevo/', prestamo_create, name='prestamo_create'),
    path('prestamos/<int:pk>/editar/', prestamo_update, name='prestamo_update'),
    path('prestamos/<int:pk>/eliminar/', prestamo_delete, name='prestamo_delete'),
]
