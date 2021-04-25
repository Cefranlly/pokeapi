import requests
from .utils.utils import build_api_url


class APICall(object):
    """
    Class base para la llamada via requests de pokeapi.co
    """
    def __init__(self, resource: str = 'pokemon'):
        self.url = build_api_url(resource)
        print("url: {}".format(self.url))

    def call_api(self, name: str = None, **kwargs):
        """
        Llamado a la API para buscar la información de pokemons siguiendo ciertos criterios de busqueda
        :param name:
        :param kwargs: parametros para querystring
        :return: retorna un json con la respuesta del request a la API
        """
        url = ""
        if name:
            url = '/'.join([self.url, name, ''])
        else:
            url = self.url

        if kwargs:
            response = requests.get(url, params=kwargs)
        else:
            response = requests.get(url)

        response.raise_for_status()

        return response.json()
