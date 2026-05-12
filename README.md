# SistemaBiblioteca

Aplicacion en Django para administrar una biblioteca.

Sistema que permite la gestion de **autores**, **libros**, **prestamos** y **usuarios** mediante un **API REST** y el uso de una interfaz web.

Este sistema fue creado utilizando Windows 11, usando PowerShell como terminal principal.

## Estructura del proyecto

En lugar de una sola aplicacion `API`, el proyecto se organiza en varias aplicaciones de Django, una por cada entidad del dominio:

```
SistemaBiblioteca/
├── SistemaBiblioteca/      # Configuracion del proyecto
├── autores/                # App para gestion de autores
├── libros/                 # App para gestion de libros
├── prestamos/              # App para gestion de prestamos
├── usuarios/               # App para gestion de usuarios
├── venv/                   # Entorno virtual
└── manage.py
```

## Configuracion de proyecto y entorno

### Instalar entorno virtual de python

```bash
python -m venv venv
```

### Activar entorno virtual (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
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

### Crear las aplicaciones del proyecto

Se crea una aplicacion por cada entidad del dominio:

```bash
python manage.py startapp autores
python manage.py startapp libros
python manage.py startapp prestamos
python manage.py startapp usuarios
```

### Registrar aplicaciones en aplicaciones instaladas

En `SistemaBiblioteca/settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'autores',
    'libros',
    'prestamos',
    'usuarios',
]
```

## Configuracion de documentacion de API usando Swagger

### Instalar `drf-spectacular-sidecar`

```bash
pip install drf-spectacular drf-spectacular-sidecar
```

`django-rest-swagger` esta deprecada por lo que se usa esta libreria recomendada por la [documentacion oficial de Django REST Framework](https://www.django-rest-framework.org/topics/documenting-your-api/).

### Agregar libreria a aplicaciones instaladas

En `SistemaBiblioteca/settings.py`:

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
    'TITLE': 'SistemaBiblioteca API',
    'DESCRIPTION': 'API REST para la gestion de autores, libros, prestamos y usuarios',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # Required for drf-spectacular-sidecar
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
```

## Como correr el proyecto

### Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario

```bash
python manage.py createsuperuser
```

### Levantar servidor de desarrollo

```bash
python manage.py runserver
```

El servidor quedara disponible en `http://127.0.0.1:8000/`.