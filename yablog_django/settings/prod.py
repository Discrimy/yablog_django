import re

from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'yablog-django.herokuapp.com'
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
USER, PASSWORD, HOST, DATABASE = re.match(
    r'mysql://(.*?):(.*?)@(.*?)/(.*?)\?reconnect=true', 
    os.environ['CLEARDB_DATABASE_URL']) \
    .groups()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE,
        'HOST': HOST,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}