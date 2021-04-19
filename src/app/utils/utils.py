
BASE_URL = 'http://pokeapi.co/api/v2'
ENDPOINTS = ['pokemon']

pokemon_keys = ['name', 'order', 'abilities', 'base_experience', 'forms','height', 'id', 'location_area_encounters',
                'moves', 'species', 'sprites', 'stats', 'types', 'weight']


def build_api_url(name, resource: str = None):
    """
    Funcion para constuir la URL que será consultada para traer los datos
    :param name: criterio de nombre de busqueda de pokemon
    :param resource: API resource para busqueda
    :return: retorna la URL a ser consultada (pokeapi.co)
    """
    validate_resource(resource)
    if name:
        return '/'.join([BASE_URL, resource, name, ''])
    return '/'.join([BASE_URL, resource, ''])


def validate_resource(resource):
    """
    Función para validar que el resource suministrado es valido
    :param resource: resource de la API
    :return: retorna un error si no es valido
    """
    if resource not in ENDPOINTS:
        raise ValueError('No existe el recurso \'{}\''.format(resource))
    return None


def dict_pokemon_converter(pokemon):
    """
    Función para tratar con la respuesta de al API pokeapi.co para el resource /POKEMON/{pokemon_name}
    :param pokemon: dict retornado por el request a la API
    :return: retorna el dict esperado con la data filtrada de un pokemon
    """
    new_pokemon = {
                "name": pokemon["name"],
                "order": pokemon["order"],
                "base_experience": pokemon["base_experience"],
                "height": pokemon["height"],
                "id": pokemon["id"],
                "location_area_encounters": pokemon["location_area_encounters"],
                "weight": pokemon["weight"],
                "abilities": [v["ability"]["name"] for v in pokemon["abilities"]],
                "forms": [v["name"] for v in pokemon["forms"]],
                "types": [v["type"]["name"] for v in pokemon["types"]],
                "moves": [v["move"]["name"] for v in pokemon["moves"]],
                "species": pokemon["species"]["name"],
                "sprites": [pokemon["sprites"]["back_default"], pokemon["sprites"]["back_shiny"],
                            pokemon["sprites"]["front_default"], pokemon["sprites"]["front_shiny"]],
                "stats": {v["stat"]["name"]: v["base_stat"] for v in pokemon["stats"]}
    }

    return new_pokemon
