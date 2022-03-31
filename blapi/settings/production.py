from blapi.settings.base import *
import os, dj_database_url
from blapi.packages.aws import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', None) == 'False'

INSTALLED_APPS.append('storages')

MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default'] = dj_database_url.parse(
    os.getenv('DATABASE_URL'),conn_max_age=600
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('static')

STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('portfolio/assets')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')