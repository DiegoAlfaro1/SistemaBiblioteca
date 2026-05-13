"""Rutas de la API REST para la gestión de préstamos."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PrestamoViewSet


# Rutas de la API REST de préstamos.
router = DefaultRouter()
router.register('prestamos', PrestamoViewSet, basename='prestamos')

urlpatterns = [
    path('', include(router.urls)),
]
