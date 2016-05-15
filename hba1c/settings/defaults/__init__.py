# Django settings for hba1c project.

import os
import copy
import djcelery

from setup_warnings import *

from os.path import join, dirname, abspath

from django.utils.log import DEFAULT_LOGGING

from .apps import *

djcelery.setup_loader()

BASE_DIR = '/usr/share/python/hba1c'

# Fallback to relative location
if not __file__.startswith(BASE_DIR):
    BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))

DEBUG = False
ALLOWED_HOSTS = ('*',)

ADMINS = (
    ('Chris Lamb', 'chris@chris-lamb.co.uk'),
)

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hba1c',
        'USER': 'hba1c',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'overriden-in-production'

MIDDLEWARE_CLASSES = (
    'django_keyerror.middleware.KeyErrorMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hba1c.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
                'hba1c.utils.context_processors.settings_context',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
                'hba1c.utils.templatetags.fonts',
                'hba1c.utils.templatetags.media',
                'hba1c.utils.templatetags.money',
                'hba1c.utils.templatetags.python',
                'hba1c.utils.templatetags.text',
            ],
        },
    },
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_DEFAULT_ACL = 'private'
AWS_ACCESS_KEY_ID = 'overriden-in-production'
AWS_SECRET_ACCESS_KEY = 'overriden-in-production'
AWS_QUERYSTRING_EXPIRE = 86400
AWS_STORAGE_BUCKET_NAME = 'overriden-in-production'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'media'),)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_FINDERS = (
    'staticfiles_dotd.finders.DotDFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CSRF_COOKIE_DOMAIN = '.hba1c.chris-lamb.co.uk'
SESSION_COOKIE_DOMAIN = '.hba1c.chris-lamb.co.uk'
SESSION_COOKIE_HTTPONLY = True

SITE_URL = 'http://hba1c.chris-lamb.co.uk'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

APPEND_SLASH = False

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

EMAIL_HOST = 'localhost'

SUPPORT_EMAIL = 'support@hba1c.co.uk'
SERVER_EMAIL = 'LetterBug <%s>' % SUPPORT_EMAIL
DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = '[hba1c] '

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'hba1c',
    }
}

# Always log to the console, even in production (ie. gunicorn)
LOGGING = copy.deepcopy(DEFAULT_LOGGING)
LOGGING['handlers']['console']['filters'] = []

KEYERROR_SECRET_KEY = 'overriden-in-production'

FONTS_ENABLED = True

BROKER_URL = 'redis://localhost:6379/0'
CELERY_IGNORE_RESULT = True
CELERY_TASK_RESULT_EXPIRES = 60
