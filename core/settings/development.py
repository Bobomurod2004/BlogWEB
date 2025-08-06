# core/settings/development.py

from .base import *
from decouple import config

# === DEVELOPMENT MODE ===
DEBUG = config('DEBUG', default=True, cast=bool)

# === ALLOWED HOSTS ===
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=lambda v: v.split(','))

# === DATABASE SETTINGS ===
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

# === STATIC FILES ===
STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']  # frontenddagi staticlar
STATIC_ROOT = BASE_DIR / 'staticfiles'    # collectstatic natijasi

# === MEDIA FILES ===
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# === EMAIL BACKEND (developmentda terminalga yuboriladi) ===
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# === SECRET_KEY (bazada bo'lmasa default qiymat ishlatiladi) ===
SECRET_KEY = config('SECRET_KEY')
