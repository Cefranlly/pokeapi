import requests
from .utils.utils import build_api_url


class APICall(object):
    """
    Class base para la llamada via requests de pokeapi.co
    """
    def __init__(self, name: str, resource: str = 'pokemon'):
        self.url = build_api_url(name, resource)
        print("url: {}".format(self.url))

    def call_api(self, **params):
        """
        Llamado a la API para buscar la información de pokemons siguiendo ciertos criterios de busqueda
        :param params: parametros para querystring
        :return: retorna un json con la respuesta del request a la API
        """
        if params:
            response = requests.get(self.url, params=params)
        else:
            response = requests.get(self.url)

        response.raise_for_status()

        data = response.json()

        return data
