from .settings import *
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

#secret for cryptography signing
SECRET_KEY = os.getenv('SECRET_KEY')

#debug configuration
DEBUG = os.getenv('DEBUG')

#database configuration
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'PORT': DB_PORT
    }
}

#project name
PROJECT_NAME = os.getenv('PROJECT_NAME')

WSGI_APPLICATION = PROJECT_NAME +'.wsgi.application'
ASGI_APPLICATION = PROJECT_NAME +'.asgi.application'

#url
ROOT_URLCONF = PROJECT_NAME + '.urls'

#allowed host
ALLOWED_HOSTS = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        'rest_framework.permissions.AllowAny'
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DEFAULT_PAGINATION_CLASS":
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 5,
}

#tokens specification
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=5),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

AUTH_USER_MODEL = 'whatsappServiceApi.User'
