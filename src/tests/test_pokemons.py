from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

"""
    Modulos de pruebas para los endpoints de busqueda de POKEMONS
"""


def test_search_pokemons(test_app):
    """
    Testcase del resource /
    :param test_app: recibe la conexión
    :return:
    """
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_search_pokemons_by_name():
    """
    Testcase del resource /{pokemon_name}
    :return:
    """
    response = client.get("/ditto")
    assert response.status_code == 200
    assert response.json() == {"name": "ditto",
                               "order": 203,
                               "abilities": [
                                   "limber",
                                   "imposter"
                               ],
                               "base_experience": 101,
                               "forms": [
                                   "ditto"
                               ],
                               "height": 3,
                               "id": 132,
                               "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/132/encounters",
                               "moves": [
                                   "transform"
                               ],
                               "species": "ditto",
                               "sprites": [
                                   "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png",
                                   "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/132.png",
                                   "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
                                   "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png"
                               ],
                               "stats": {
                                   "hp": 48,
                                   "attack": 48,
                                   "defense": 48,
                                   "special-attack": 48,
                                   "special-defense": 48,
                                   "speed": 48
                               },
                               "types": [
                                   "normal"
                               ],
                               "weight": 40
                               }
