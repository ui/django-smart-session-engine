# -*- coding: utf-8 -*-
import django
import os
from distutils.version import StrictVersion

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 36000,
        'KEY_PREFIX': 'smart-session',
    },
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
)

SECRET_KEY = 'a'

DEFAULT_FROM_EMAIL = 'webmaster@example.com'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'tests/static')]


SESSION_ENGINE = "libraries.smart_session_engine.session_engine"
SMART_SESSION_ENGINE_CONNECTION_URL = "redis://127.0.0.1:6379/1"
