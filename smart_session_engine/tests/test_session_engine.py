from django.test import TestCase

from smart_session_engine.session_engine import SessionStore
from smart_session_engine.utils import get_redis_connection


class SessionEngineTest(TestCase):

    def setUp(self):
        self.redis = get_redis_connection()

    def cleanup_redis(self):
        redis = get_redis_connection()
        for key in redis.keys("smart-session-test*"):
            redis.delete(key)

        for key in redis.keys("session_id*"):
            redis.delete(key)

    def test_save(self):
        self.cleanup_redis()

        session = SessionStore(session_key="aaaaaaaa1234")
        session["_auth_user_id"] = "123"
        session.save()

        # Make sure the set is created correctly
        self.assertEqual(self.redis.scard(session._get_user_mapping_key("123")), 1)

        # Every time user logs in, the mapping is updated
        session = SessionStore(session_key="aaaaaaaa1235")
        session["_auth_user_id"] = "123"
        session.save()
        self.assertEqual(self.redis.scard(session._get_user_mapping_key("123")), 2)
