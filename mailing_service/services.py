from django.core.cache import cache

from config.settings import CACHE_ENABLED
from mailing_service.models import Mailing


def get_mailings_from_cache():
    """ Получает данные по рассылкам из кэша, если кэш пуст, получает данные из БД """

    if not CACHE_ENABLED:
        return Mailing.objects.all()
    key = 'mailings_list'
    mailings = cache.get(key)
    if mailings is not None:
        return mailings
    mailings = Mailing.objects.all()
    cache.set(key, mailings)
    return mailings
