from .utils import get_redis_connection

from django.contrib.sessions.backends.cache import SessionStore as CacheSessionStore


class SessionStore(CacheSessionStore):

    def save(self, *args, **kwargs):
        must_create = kwargs.get('must_create', False)
        super(SessionStore, self).save(must_create)

        redis = get_redis_connection()
        user_id = self._get_session(no_load=must_create).get('_auth_user_id', None)
        if user_id:
            redis.sadd("session_id:%s" % user_id, self.session_key)

    def delete(self, session_key=None):
        redis = get_redis_connection()
        session_key = session_key or self.session_key
        user_id = self.load().get('_auth_user_id', None)
        if user_id:
            redis.srem("session_id:%s" % user_id, session_key)

        super(SessionStore, self).delete(session_key)
