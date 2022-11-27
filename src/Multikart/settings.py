"""
Django settings for Multikart project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path


import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%9a5=j+bb^ar4_qfcnb-=m-2$#aun$c1pamm03^@8l8^nho6*s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'core/locale'),
)



LOCAL_APPS = [
    'product','order','users','core','authorization', 'all_logs', 'all_images', 'emails','api', 
]

INSTALLED_APPS = [
 
   
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
    *LOCAL_APPS, 
   
 
    'logging_middleware',
    'rest_framework',
    "verify_email.apps.VerifyEmailConfig",
    'django_celery_beat',
    

]
DJANGO_LOGGING_MIDDLEWARE = {
    'DEFAULT_FORMAT': True,
    'MESSAGE_FORMAT': "<b><green>{time}</green> <cyan>{message}</cyan></b>",
    'LOG_USER': False
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'all_logs.middlewares.DjangoLoggingMiddleware',
    'emails.middlewares.SetLastVisitMiddleware',
    
    
]

CACHE_MIDDLEWARE_ALIAS = 'default'  
CACHE_MIDDLEWARE_SECONDS = 15
CACHE_MIDDLEWARE_KEY_PREFIX = '' 


EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL=f'Celery {EMAIL_HOST_USER}'



WSGI_APPLICATION = 'Multikart.wsgi.application'


ROOT_URLCONF = 'Multikart.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "webappexample", "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "users.context_processors.user",
                "core.context_processors.subscribe_form"
                
            ],
        },
    },
]



WSGI_APPLICATION = 'Multikart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'), 
        'USER': os.getenv('DB_USER'), 
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'DISABLE_SERVER_SIDE_CURSORS': True
    },

    'mongodb':  {
            'ENGINE': 'djongo',
            'NAME': 'Multikart_mongo',
      
            

       
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = "users.User" 

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/


TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# from django.utils.translation import gettext_lazy as _
# LANGUAGE_CODE = 'en-us'


# LANGUAGES = (
#     ('en', _('English')),
#     ('ru', _('Russian')),

# )

# MODELTRANSLATION_TRANSLATION_FILES = (
#     'core.translation',
#     'order.translation',
#     'product.translation',
#     'users.translation',
#     # 'all_logs.translation'

# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = 'src/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)



# Load Auth0 application settings into memory
    AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
    AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
    AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")


    

from celery import Celery
os.environ.setdefault('DJANGO_SETTING_MODULE' , 'multikart.settings')

app = Celery ('multikart')

app.config_from_object('django.conf:settings' , namespace='CELERY')
CELERY_TIMEZONE = TIME_ZONE


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"