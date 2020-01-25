import os

from config.dev.settings import *

DEBUG = False

WSGI_APPLICATION = 'config.prd.app.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('BadBall_DB_NAME', 'badball'),
        'USER': os.environ.get('BadBall_DB_USER', 'ubuntu'),
        'PASSWORD': os.environ.get('BadBall_DB_PASS', ''),
        'HOST': os.environ.get('BadBall_DB_HOST', ''),
    }
}

STATIC_ROOT = '/var/www/thebadball.com/static'
STATIC_URL = '/static/'

ALLOWED_HOSTS = ['*']