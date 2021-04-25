# pokemon_api

API para la exponer la data de los pokemons (https://pokeapi.co/docs/v2)

## Table of Content
- [Project structure](#Project-structure)
- [Prerequisites](#Prerequisites)
- [Setup environment](#Setup-environment)
- [How to run it?](#How-to-run-it)
- [How to test it?](#How-to-test)
- [Contributing](#Contributing)


## Project-structure

```
pokemon
├── src
│   ├── requirements.txt     # Archivo con las librerías necesarias para el proyecto
│   ├── Dockerfile           # Archivo de config de docker para levantar la app
│   ├── app                  # "app" is a Python package
│   │   ├── __init__.py      # Modulo
│   │   └── api              # Modulo que contiene los modelos de datos y los endpoints 
│   │   └── utils            # Modulo que contiene archivos python con utilities
│   ├── tests                # Directorio con archivos de prueba
│   │   ├── __init__.py      # Modulo
│   │   ├── configtest.py    # Fixture config
│   │   └── test_pokemons.py # testcases para los endpoints
│   └── postman              # collection postman para consultar los endpoints 
└── docker-compose.yml    # Archivo de configuración para levantar servicio  

```

## Prerequisites

- fastapi==0.63.0
- pydantic==1.8.1
- starlette==0.13.6
- typing-extensions==3.7.4.3
- uvicorn==0.13.4
- pytest==5.3.2
- requests==2.22.0

## Setup-environment

- Install [Docker](https://docs.docker.com/install/)
- Install [Python](https://www.python.org/downloads/)
- [Clonar el proyecto](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
- Ubicate en el root del proyecto y ejecuta el siguiente comando:
  
    ``docker-compose up -d --build``

## How-to-run-it

Debes ejecutar el siguiente comando para levantar la app:

``docker-compose up -d``

Para "apagar" el servicio:

``docker-compose -f docker-compose.yml stop``

Una vez este arriba la app, podes probar los endpoints usando [Postman](https://learning.postman.com/docs/getting-started/installation-and-updates/)
y cargando la [colección](https://developer.ft.com/portal/docs-start-install-postman-and-import-request-collection) para su consumo

API Resources:

```
Obtener listado de pokemons

GET /

q: string -> posible nombre del pokemon
limit: integer -> número límite de pokemones a retornar en al consult
offset: integer -> rango de offset para la búsqueda 
```

```
Obtiene los datos de un pokemon por su nombre

GET /{pokemon_name} 
```

## How-to-test

Al tener instalado el pytest y haber generado los modulos de pruebas, puedes correr:

``docker-compose exec web pytest .``

Una vez levanta la App, conoce mas de los endpoints en [docs](http://localhost:8002/docs)

## Contributing

- [Cefranlly Pérez](cefranllyperez@gmail.com)


**PD:** perdón el spanglish