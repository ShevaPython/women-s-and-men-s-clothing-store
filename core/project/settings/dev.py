import os

from .base import *
from .utils import load_environment

load_environment('.env.dev', basedir=BASE_DIR)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/sheva/Рабочий стол/dropshipping/db.sqlite3',
    }
}
