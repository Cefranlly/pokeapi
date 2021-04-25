from typing import List, Dict
from pydantic import BaseModel


class PokemonDetail(BaseModel):
    """
    Class con el objecto de datos base de respuesta de la API /{pokemon_name}
    """
    name: str
    order: int
    abilities: List[str]
    base_experience: int
    forms: List[str]
    height: int
    id: int
    location_area_encounters: str
    moves: List[str]
    species: str
    sprites: List[str]
    stats: Dict[str, int]
    types: List[str]
    weight: int


class Pokemons(BaseModel):
    """
    Class con el objecto de datos base de respuesta de la API /
    """
    total: int
    limit: int
    offset: int
    data: List
