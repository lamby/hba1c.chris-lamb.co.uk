from local import *

DATABASES['default'].update({
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    'ATOMIC_REQUESTS': True,
})

MEDIA_ROOT = '/tmp'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
