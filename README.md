# SistemaBiblioteca

SistemaBiblioteca es una aplicacion Django para administrar una biblioteca.

Permite gestionar autores, libros, usuarios y prestamos mediante una API REST, ademas de una interfaz web sencilla para administrar los prestamos.

## Caracteristicas

- CRUD de autores, libros, usuarios y prestamos desde API REST.
- Interfaz web para listar, crear, editar y eliminar prestamos.
- La ruta base `/` redirige al listado de préstamos.
- Validaciones de negocio para evitar fechas invalidas y prestamos duplicados sobre el mismo libro.
- Documentacion de la API con Swagger y OpenAPI.
- Página 404 personalizada en español.
- Panel de administracion de Django para gestionar los modelos desde la interfaz nativa.

## Estructura del proyecto

```text
SistemaBiblioteca/
├── SistemaBiblioteca/      Configuracion general del proyecto
├── autores/                Modelo, API y admin de autores
├── libros/                 Modelo, API y admin de libros
├── prestamos/              Modelo, API, vistas web y formularios de prestamos
├── usuarios/               Modelo, API y admin de usuarios
├── templates/              Plantilla base compartida
├── db.sqlite3              Base de datos local
└── manage.py
```

## Endpoints

### API REST

- `GET /api/autores/`
- `GET /api/libros/`
- `GET /api/usuarios/`
- `GET /api/prestamos/`
- `GET /api/schema/`
- `GET /api/docs/`

### Interfaz web

- `GET /` redirige a `/prestamos/`
- `GET /prestamos/`
- `GET /prestamos/nuevo/`
- `GET /prestamos/<id>/editar/`
- `GET /prestamos/<id>/eliminar/`

### Página de error

- `404` personalizada en español para rutas no encontradas.

### Panel de administracion

- `GET /admin/`

## Requisitos

- Python 3.11 o superior
- pip
- Entorno virtual de Python

## Instalacion

1. Crear el entorno virtual.

```bash
python -m venv venv
```

2. Activar el entorno virtual en PowerShell.

```powershell
.\venv\Scripts\Activate.ps1
```

3. Instalar dependencias.

```bash
pip install django djangorestframework drf-spectacular drf-spectacular-sidecar
```

## Como ejecutar el proyecto

1. Aplicar migraciones.

```bash
python manage.py migrate
```

2. Crear un superusuario para acceder al panel de administracion.

```bash
python manage.py createsuperuser
```

3. Iniciar el servidor de desarrollo.

```bash
python manage.py runserver
```

4. Abrir el navegador en la direccion local.

```text
http://127.0.0.1:8000/
```

## Notas de uso

- La base de datos local utiliza SQLite y se guarda en `db.sqlite3`.
- La interfaz web principal de prestamos usa las plantillas dentro de `prestamos/templates/prestamos/`.
- La plantilla `templates/404.html` se usa para mostrar un error 404 personalizado.
- Para ver la página 404 personalizada, el proyecto se ejecuta con `DEBUG = False` y `ALLOWED_HOSTS` configurado.
- La documentacion Swagger esta disponible en `http://127.0.0.1:8000/api/docs/`.

## Observacion

Este proyecto esta orientado a desarrollo local. Para despliegue en produccion se recomienda revisar `DEBUG`, `ALLOWED_HOSTS`, la clave secreta y la configuracion de la base de datos.
