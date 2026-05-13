"""Rutas de la API REST para la gestión de libros."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet

router = DefaultRouter()
router.register('libros', LibroViewSet, basename='libros')

urlpatterns = [
    path('', include(router.urls)),
]

