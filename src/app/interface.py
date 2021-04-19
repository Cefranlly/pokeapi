from app.apicall import APICall
from app.utils.utils import dict_pokemon_converter


def get_pokemons(q: str, limit: int, offset: int):
    """
    Consulta y retorna la data de una lista de pokemon por un filter criteria
    :param q: nombre del pokemon
    :param limit: limite de pokemons traidos en la consulta
    :param offset: rango de registros a traer por la consulta
    :return: dict con la lista de pokemon traidos de la consulta
    """
    api_call = APICall(q, limit, offset, 'pokemon')
    return api_call.get_data()


def get_pokemon_by_name(name: str):
    """
    Consulta la data de un pokemon por su nombre
    :param name: nombre del pokemon a buscar
    :return: dict con la data del pokemon consultado
    """
    api_call = APICall(name, 'pokemon')
    result = dict_pokemon_converter(api_call.call_api())
    return result

