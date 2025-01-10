# {{ cookiecutter.project_name }}

![Static Badge](https://img.shields.io/badge/Estatus-En%20Desarrollo-yellow)
![Static Badge](https://img.shields.io/badge/Versi%C3%B3n-1.0.0-blue)
![Static Badge](https://img.shields.io/badge/Lenguaje-Python-blue)
![Static Badge](https://img.shields.io/badge/Pruebas-En%20Desarrollo-yellow)

## **Descripción General**

{{ cookiecutter.short_description_project }}

## Índice

* [Requisitos de Instalación](#requisitos-de-instalación)
* [Guía de Configuración](#guía-de-configuración)
* [Descripción de Endpoints](#descripción-de-endpoints)
* [Pruebas](#pruebas)

## Requisitos de Instalación

Para ejecutar **{{ cookiecutter.project_name }}**, necesitas tener instalados los siguientes programas:

### Instalación de Docker
- [Docker](https://docs.docker.com/get-docker/): Para gestionar contenedores.

### Instalación de Docker Compose
- [Docker-compose](https://docs.docker.com/compose/install/): Para definir y ejecutar aplicaciones multi-contenedor.

## Guía de Configuración

### Configurar el archivo .env

Crea un archivo _.env_ en la base del proyecto con las siguientes variables

```bash
HOST={{ cookiecutter.host }}
PORT={{ cookiecutter.port }}

# AMBIENTE DE LA APLICACIÓN (elegir una opción)
ENVIRONMENT=<'production', 'development', 'staging'>

# RUTA BASE
BASE_URL={{ cookiecutter.base_url }} # Para producción

# Configuración del servidor SMTP
SMTP_ID_SERVICE=<identificador_smtp_example>
SMTP_SERVER=smtp-example.com
SMTP_PORT=587 # TLS
SMTP_USER=<smtp_user>
SMTP_PASSWORD=<smtp_password>
```

### Construir y Levantar los Contenedores

Ejecuta los siguientes comandos para construir y levantar los contenedores:

```bash
docker-compose build
docker-compose up -d
```
Para detener el servicio, ejecutar el siguiente comando en la terminal:

```bash
docker-compose down -v
```

## Descripción de Endpoints


## Pruebas