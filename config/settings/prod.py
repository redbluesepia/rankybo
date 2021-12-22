from .base import *

ALLOWED_HOSTS = ['54.180.207.198', 'rankystock.com']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rankybo',
        'USER': 'redblues',
        'PASSWORD': 'i^mredsp6l',
        'HOST': '54.180.207.198',
        'PORT': '5432',
    }
}