# myproject/settings/production.py
from .base import *

DEBUG = True

# Xavfsiz hostlarni kiriting
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=lambda v: v.split(','))

# PostgreSQL yoki boshqa baza
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static va media fayllar serverga chiqadi
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
print("DATABASE_ENGINE:", config('DATABASE_ENGINE', default='NO_ENGINE_FOUND'))

