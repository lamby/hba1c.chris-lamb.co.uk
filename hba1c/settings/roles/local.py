from os.path import join, dirname, abspath, normpath

def base_dir(*paths):
    return join(
        dirname(dirname(dirname(dirname(normpath(__file__))))),
        *paths
    )

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hba1c',
        'ATOMIC_REQUESTS': True,
    },
}

CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False

SITE_URL = 'http://127.0.0.1:8000'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_URL = '/storage/'
MEDIA_ROOT = base_dir('storage')

BROKER_URL = 'memory://'
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
