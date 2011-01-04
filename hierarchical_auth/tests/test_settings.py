import os

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'mptt',
    'hierarchical_auth',
    'hierarchical_auth.tests',
)

DATABASE_ENGINE = 'sqlite3'

AUTHENTICATION_BACKENDS = (
    'hierarchical_auth.backends.HierarchicalModelBackend',
)
