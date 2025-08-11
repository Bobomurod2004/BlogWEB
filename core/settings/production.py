# myproject/settings/production.py
from .base import *

DEBUG = False

# Xavfsiz hostlarni kiriting
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=lambda v: v.split(','))
ALLOWED_HOSTS = ["<your-domain.com>", "<IP-adress-or-host>", "localhost"]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Logging (xatoliklarni kuzatish)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

# Static va media fayllar serverga chiqadi
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
print("DATABASE_ENGINE:", config('DATABASE_ENGINE', default='NO_ENGINE_FOUND'))

