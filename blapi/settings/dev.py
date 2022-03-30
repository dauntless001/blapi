from blapi.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gvs@wc#j0=(_%(&e5-za_d7j2wy4#bwue09mge%thg0ioo2d&u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'blapi.db',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('blapi/assets')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')