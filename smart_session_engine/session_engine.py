from .utils import get_redis_connection

from django.contrib.sessions.backends.cache import SessionStore as CacheSessionStore


class SessionStore(CacheSessionStore):

    def _get_key(self, user_id):
        # What we want
        # return "%s:session_id:%s" % (self._cache.key_prefix, user_id)

        # This is the original
        return "session_id:%s" % user_id

    def save(self, *args, **kwargs):
        must_create = kwargs.get('must_create', False)
        super(SessionStore, self).save(must_create)

        redis = get_redis_connection()
        user_id = self._get_session(no_load=must_create).get('_auth_user_id', None)
        if user_id:
            key = self._get_key(user_id)
            pipeline = redis.pipeline()
            pipeline.sadd(key, self.session_key)
            pipeline.expire(key, self._cache.default_timeout)
            pipeline.execute()

    def delete(self, session_key=None):
        """ This only triggered on explicit logout """
        redis = get_redis_connection()
        session_key = session_key or self.session_key
        user_id = self.load().get('_auth_user_id', None)
        if user_id:
            redis.srem(self._get_key(user_id), session_key)

        super(SessionStore, self).delete(session_key)
