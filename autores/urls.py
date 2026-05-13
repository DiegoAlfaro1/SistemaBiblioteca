from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AutorViewSet

router = DefaultRouter()
router.register('autores', AutorViewSet, basename='autores')

urlpatterns = [
    path('', include(router.urls)),
]
