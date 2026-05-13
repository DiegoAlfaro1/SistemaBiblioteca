"""
Rutas principales del proyecto SistemaBiblioteca.

Conecta el panel de administración, los endpoints REST, las vistas HTML
de préstamos y la documentación de la API.
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints de la API REST.
    path('api/', include('autores.urls')),
    path('api/', include('libros.urls')),
    path('api/', include('usuarios.urls')),
    path('api/', include('prestamos.urls')),

    # Vistas HTML de préstamos.
    path('', include('prestamos.web_urls')),

    # Documentación OpenAPI y Swagger.
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
