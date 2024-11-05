from django.core.cache import cache

from clients.models import Client
from config.settings import CACHE_ENABLED


def get_clients_from_cache():
    """ Получает данные по клиентам из кэша, если кэш пуст, получает данные из БД """

    if not CACHE_ENABLED:
        return Client.objects.all()
    key = 'clients_list'
    clients = cache.get(key)
    if clients is not None:
        return clients
    clients = Client.objects.all()
    cache.set(key, clients)
    return clients
