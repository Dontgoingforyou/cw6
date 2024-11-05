from django.core.cache import cache

from config.settings import CACHE_ENABLED
from message.models import Message


def get_messages_from_cache():
    """ Получает данные по сообщениям из кэша, если кэш пуст, получает данные из БД """

    if not CACHE_ENABLED:
        return Message.objects.all()
    key = 'messages_list'
    messages = cache.get(key)
    if messages is not None:
        return messages
    messages = Message.objects.all()
    cache.set(key, messages)
    return messages
