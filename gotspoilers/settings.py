import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'characters',
)

DATABASES = {'default': dj_database_url.parse(os.environ['DATABASE_URL'])}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FOAUTH_USERNAME = os.environ['FOAUTH_USERNAME']
FOAUTH_PASSWORD = os.environ['FOAUTH_PASSWORD']
