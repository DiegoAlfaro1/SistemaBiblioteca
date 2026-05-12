from SistemaBiblioteca.settings import INSTALLED_APPSfrom SistemaBiblioteca.settings import INSTALLED_APPS

# SistemaBiblioteca
Aplicacion en Django para administrar una biblioteca

Sistema que permite la gestion de autores, libros y prestamos mediante un **API REST** y el uso de una interfaz web.

Este sistema fue creado utilizando windows 11, usando poweshell como terminal principal

## Configuracion de proyecto y entorno

### Instalar entorno virtual de python

```bash
python -m venv venv
```

### Instalar Django

```bash
pip install django
```

### Iniciar proyecto de django en repositorio

```bash
django-admin startproject SistemaBiblioteca .
```

### Instalar framework REST de django
```bash
pip install djangorestframework
```

### Iniciar API REST con nombre ``API``
```bash
python manage.py startapp API
```

### Registrar aplicacion en aplicaciones instaladas
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'API',
]
```

## Configuracion de documentacion de API usando swagger

### Instalar ``drf-spectacular-sidecar``

```bash
pip install drf-spectacular drf-spectacular-sidecar
```
``django-rest-swagger`` esta deprecada por lo que se usa esta libreria recomendada por la [documentacion oficial de django](https://www.django-rest-framework.org/topics/documenting-your-api/)

### Agregar libreria a aplicaciones instaladas

```python
INSTALLED_APPS = [
    ...,
    'drf_spectacular',
    'drf_spectacular_sidecar',
]
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Detailed description of your API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # Required for drf-spectacular-sidecar
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
```


