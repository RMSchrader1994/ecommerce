from .base import *

DEBUG = True

INSTALLED_APPS.append('storages')

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (STATICFILES_LOCATION)