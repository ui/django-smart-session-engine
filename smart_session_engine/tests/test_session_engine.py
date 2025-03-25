import django
import os


from django.test import TestCase

from smart_session_engine.session_engine import SessionStore
from smart_session_engine.utils import get_redis_connection


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_session_engine.tests.settings")

django.setup()


# Simulate django user class with id
class User:
    id: int

    def __init__(self, id: int):
        self.id = id


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
        self.assertEqual(self.redis.scard(session._get_key("123")), 1)

        # Every time user logs in, the mapping is updated
        session = SessionStore(session_key="aaaaaaaa1235")
        session["_auth_user_id"] = "123"
        session.save()
        self.assertEqual(self.redis.scard(session._get_key("123")), 2)

    def test_delete_multiple_session_keys(self) -> None:
        user1 = User(id=5678921)
        user2 = User(id=5678922)
        user3 = User(id=5678923)

        self.cleanup_redis()

        session = SessionStore(session_key="aaaaaaaa1111")
        session["_auth_user_id"] = str(user1.id)
        session.save()

        # User 1 login again
        session = SessionStore(session_key="aaaaaaaa1112")
        session["_auth_user_id"] = str(user1.id)
        session.save()

        self.assertEqual(self.redis.scard(session._get_key(str(user1.id))), 2)

        session = SessionStore(session_key="aaaaaaaa2221")
        session["_auth_user_id"] = str(user2.id)
        session.save()

        self.assertEqual(self.redis.scard(session._get_key(str(user2.id))), 1)

        session = SessionStore(session_key="aaaaaaaa3331")
        session["_auth_user_id"] = str(user3.id)
        session.save()
        self.assertEqual(self.redis.scard(session._get_key(str(user3.id))), 1)

        # Delete all keys for user 1 & 2
        SessionStore().delete_many([user1, user2])
        self.assertEqual(self.redis.scard(session._get_key(str(user1.id))), 0)
        self.assertEqual(self.redis.scard(session._get_key(str(user2.id))), 0)
        # Still 1 since we didn't delete user3 session keys
        self.assertEqual(self.redis.scard(session._get_key(str(user3.id))), 1)
