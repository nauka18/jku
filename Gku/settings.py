"""
Django settings for Gku project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOSTNAME = '127.0.0.1:8000'
if not DEBUG:
    HOSTNAME == '212.47.134.12:8000'

SERVER_IP = '212.47.227.134'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '##q!fj^cn(0^&&w#f-p-xm$tieppkkp4=g^rqs@77l_ts^5ywk'

ALLOWED_HOSTS = ['*']

# EMAIL settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cypherdesk.isyn@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_PASSWORD = 'HackersChoose1syn'


RECAPTCHA_PRIVATE_KEY = '6LegpHoUAAAAAKZkDl-QmJQ9wAVAeVvKtdPGCgDz'
RECAPTCHA_PUBLIC_KEY = '6LegpHoUAAAAACQoehcT3E57XpBbBi3XnFnqAIUl'

# Application definition

INSTALLED_APPS = [
    'snowpenguin.django.recaptcha2',
    'Account',
    'LandPage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Gku.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Gku.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gku',
        'USER': 'suriknik',
        'PASSWORD': '6dLm0kSS7z33',
        'HOST': 'localhost',
        'PORT': '',
    }
}

FEEDBACK_TELEGRAM_BOT_KEY = '560497318:AAFApTmjXY-3OgCPutovBW230x82d5ep08Y'
FEEDBACK_TELEGRAM_CHAT_ID = 560497318

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CSRF_COOKIE_SECURE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


AES_DEFAULT_KEY = 'K3kL01ArB1D0L228K3kL01ArB1D0L228'
AES_ACTIVATION_KEY = 'qwertyL0xqwertyL0xqwertyL0xqwert'
AES_ID_KEY = 'importantEducaT10NimportantEduca'
AES_DEFAULT_IV = b'\x83\xc5\x13\xfev\xeb<\x80@\xb1\xc4`\x89\x10\x01\xa7'