
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h%2j5s$v0gx4+wcc$-uek9k_@76!yx@xi3wy_h+33k*5d9ok73'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webservice.apps.WebserviceConfig',
    'crispy_forms',
    'rest_framework',
    'api.apps.ApiConfig',
    'drf_yasg',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forum_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'forum_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'forums',
        # 'USER': 'postgres',
        # 'PASSWORD': 'Sos445566',
        # 'PORT': '5432',
        # 'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    #{
      #  'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
     #   'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
     #   'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIRS = [
    os.path.join(BASE_DIR, '/static')
]

STATIC_ROOT =os.path.join(BASE_DIR, "root/static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587 
EMAIL_HOST_USER = "iljasergeevich1995@gmail.com"
EMAIL_HOST_PASSWORD = "Bag337799"
EMAIL_USE_TLS = True

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 10
# }

LOGGING = {
    'version': 1,
    'dissable_existing_loggers': False,
    'formatters': {
        'simple':{
            'format':'[%(asctime)s] %(levelname)s  %(message)s',
            'datefmt': '%Y.%m.%d %H:%M:%S',
            }
        },
    'filters': {
        'require_debug_true':{
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false':{
             '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console_prod':{
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_false'],
            'level': 'ERROR'
            },
        'console_debug':{
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
            'level': 'DEBUG'
            },
        'file':{
            'class':'logging.FileHandler',
            'filename': BASE_DIR / 'logs/forum_api.log',
            'level': 'INFO',
            'formatter': 'simple',
            },
    },
    'loggers': {
        'django':{
        'handlers':['console_debug', 'file'],
        },  
    },
    
}