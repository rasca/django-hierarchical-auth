import os

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'hierarchical_auth',
        'hierarchical_auth.tests',
        )

DATABASE_ENGINE = 'sqlite3'

