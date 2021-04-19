from fastapi import APIRouter, HTTPException
from app.api.models import PokemonDetail, Pokemon
from typing import Optional, List
from app.interface import get_pokemon_by_name as get_by_name, get_pokemons

router = APIRouter()


# Pokemons route
@router.get("/", response_model=List[Pokemon], status_code=200)
async def get_pokemons(q: Optional[str] = None, limit: Optional[int] = 10, offset: Optional[int] = 0):
    """
    Endpoint para busqueda de pokemons segun parametrias
    :param q: Nombre o parte de nombre de los pokemons
    :param limit: limite a retornar en la busqueda
    :param offset: rango de busqueda
    :return: Lista de pokemons
    """
    pokemon_result = await get_pokemons(q, limit, offset)
    raise HTTPException(status_code=404, detail="Pokemons endpoint DIDN'T FIND any match for your searching criteria!!!")
    return pokemon_result


# Pokemon by name
@router.get("/{pokemon_name}/", response_model=PokemonDetail, status_code=200, tags=["pokemon"])
async def get_pokemon_by_name(pokemon_name: str):
    """
    Endpoint para busqueda de un pokemon por su nombre
    :param pokemon_name: Nombre del pokemon a buscar
    :return: Retorna los datos de un pokemon segun el nombre
    """
    pokemon_result = get_by_name(pokemon_name)
    if not pokemon_result:
        raise HTTPException(status_code=404, detail="Pokemon NOT FOUND!")
    return pokemon_result
