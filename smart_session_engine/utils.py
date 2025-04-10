from redis import Redis

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_user_key(user_id):
    # What we want
    # return "%s:session_id:%s" % (self._cache.key_prefix, user_id)

    # This is the original
    return "session_id:%s" % user_id


def get_redis_connection():
    redis_url = getattr(settings, 'SMART_SESSION_ENGINE_CONNECTION_URL', None)

    if redis_url is None:
        raise ImproperlyConfigured("You have to define SMART_SESSION_ENGINE_CONNECTION_URL in settings.py")

    return Redis.from_url(redis_url)


def delete_session_keys(user):
    from .session_engine import SessionStore
    redis = get_redis_connection()
    key = get_user_key(user.id)
    for session_key in redis.smembers(key):
        SessionStore().delete(session_key=session_key)
    redis.delete(key)
