"""
Configuración principal del proyecto SistemaBiblioteca.

Este archivo define las aplicaciones instaladas, la base de datos,
las plantillas, la integración con Django REST Framework y la
documentación OpenAPI con drf-spectacular.
"""

from pathlib import Path

# Ruta base del proyecto para construir rutas relativas.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración pensada para desarrollo local.

# Mantener esta clave secreta fuera de producción.
SECRET_KEY = 'django-insecure-u3h^^o!rk^wn9^z$@-_6jhp7e+z@o!ho&*wj6f060&6-c_^392'

# No usar DEBUG=True en producción.
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Aplicaciones instaladas en el proyecto.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework',
    'autores',
    'libros',
    'prestamos',
    'usuarios',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'SistemaBiblioteca API',
    'DESCRIPTION': 'API REST para la gestion de autores, libros, prestamos y usuarios',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # Requerido por drf-spectacular-sidecar
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SistemaBiblioteca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SistemaBiblioteca.wsgi.application'


# Base de datos local SQLite.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validadores de contraseñas de Django.

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización y zona horaria.

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Archivos estáticos.

STATIC_URL = 'static/'

# Tipo de campo por defecto para claves primarias.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
