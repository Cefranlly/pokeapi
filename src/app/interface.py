from app.apicall import APICall
from app.utils.utils import dict_pokemon_converter, extract_pokemon_data
from re import search


def get_all_pokemons(q: str, limit: int = 100, offset: int = 0):
    """
    Consulta y retorna la data de una lista de pokemon por un filter criteria
    :param name: nombre del pokemon
    :param q: nombre del pokemon
    :param limit: limite de pokemons traidos en la consulta
    :param offset: rango de registros a traer por la consulta
    :return: dict con la lista de pokemon traidos de la consulta
    """
    poke_list = []
    # Necesitamos iterar sobre la respuesta de todos los pokemons
    api_call = APICall('pokemon')
    data_result = api_call.call_api(limit=limit, offset=offset)

    for pokemon in data_result["results"]:
        if q:
            if search(q, pokemon["name"]):
                poke_list.append(extract_pokemon_data(api_call.call_api(pokemon["name"])))
        else:
            poke_list.append(extract_pokemon_data(api_call.call_api(pokemon["name"])))

    return {
        "total": data_result["count"],
        "offset": offset,
        "limit": limit,
        "data": poke_list
    }


def get_pokemon_by_name(name: str):
    """
    Consulta la data de un pokemon por su nombre
    :param name: nombre del pokemon a buscar
    :return: dict con la data del pokemon consultado
    """
    api_call = APICall('pokemon')
    result = dict_pokemon_converter(api_call.call_api(name))
    return result

