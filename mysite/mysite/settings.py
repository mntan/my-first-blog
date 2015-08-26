"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')w=bb1im-zb+v^xyu@7+w6$s6(11kx4!47jpvmr8bmbcreeb&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'polls',
    's3sync', 
    'redis_cache',   
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'mysite',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
    }
}
CACHES = {
    'default': {
        'BACKEND':'redis_cache.RedisCache',
        'LOCATION':'http://127.0.0.1:6379/',
        'TIMEOUT':3600*24*30,
        'OPTIONS':{
            'DB':2,
        }
    },
    's3-storage' : {
        'BACKEND':'redis_cache.RedisCache',
        'LOCATION':'http://127.0.0.1:6379/',
        'TIMEOUT':3600*24*30,
        'OPTIONS':{
            'DB':2,
        }
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#AUTH_USER_MODEL = 'myauth.User'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 's3sync.storage.S3PendingStorage'

AWS_ACCESS_KEY_ID = 'AKIAJLBBQSEW4QQ45UVA'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET_UPLOADS = 'coolertesttest'
BUCKET_UPLOADS_URL = '//coolertesttest.s3-website-ap-southeast-1.amazonaws.com/'
BUCKET_ASSETS_PREFIX = 'media'
BUCKET_UPLOADS_PREFIX = 'media/uploads'
BUCKET_UPLOADS_PATH = MEDIA_ROOT + '/profile'
BUCKET_UPLOADS_CACHE_ALIAS = 's3-storage'
BUCKET_UPLOADS_PENDING_KEY = 's3-pending'
BUCKET_UPLOADS_PENDING_DELETE_KEY = 's3-pending-delete'
# For your production site, link to the S3 uploads bucket.
# This setting is optional for development.
PRODUCTION = True