"""
Django settings for vacation_feast_Website project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import pymysql
import os

pymysql.version_info = (1,4,6,'final',0)
pymysql.install_as_MySQLdb

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b42)-c7s$rn7k0)-_3e%5--&h_pvy5@n+yr_-*l3u*w6ht_3dp'

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
    'VFpages',
    'admin_panel',
    'captcha',
    'booking',
    'payment',
    'flight'
]

CAPTCHA_IMAGE_SIZE = (150, 50)
CAPTCHA_FONT_SIZE = 32
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'vacation_feast_Website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'VFpages','templates')],
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

WSGI_APPLICATION = 'vacation_feast_Website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vacationfeast',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'gokulraj',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    },
    'second_database': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newmain',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'gokulraj',
        'PORT': '3306',
    }

}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/VFpages/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'VFpages', 'static'),
#     os.path.join(BASE_DIR, 'admin_panel', 'static'),
#     # Add other app static directories if needed
# ]

# # Directory where static files will be collected during deployment
STATIC_ROOT = os.path.join(BASE_DIR,'VFpages', 'static')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024 * 1024  # 100 GB (in bytes)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtppro.zoho.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'gokulraj@vacationfeast.com'
EMAIL_HOST_PASSWORD = 'gokulraj@123'


GALLABOX_API_KEY = '63c4f8e4da6a679a061f84e4'
GALLABOX_API_SECRET = '055c76989ae94746b5f861464c387066'
GALLABOX_CHANNELID = '63b7e6ff3749160e1e2d36c2'


SESSION_COOKIE_AGE = 86400


RAZORPAY_MERCHANT_KEY = 'rzp_test_5bpcghNaRd7Qqg'
RAZORPAY_MERCHANT_SECRET = 'AyBHtno3opb2r4D1pVgqpPG5'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# import os
# from cryptography.fernet import Fernet

# # Retrieve the secret key from the environment variable
# SECRET_KEY = os.environ.get('SECRET_KEY')

# # If no secret key is found, generate a new one
# if not SECRET_KEY:
#     # Generate a new key
#     generated_key = Fernet.generate_key()
    
#     # Convert the generated key to a string
#     SECRET_KEY = generated_key.decode()

#     # Store the key securely in the environment variables
#     os.environ['SECRET_KEY'] = SECRET_KEY

# # Initialize Fernet with the secret key
# fernet = Fernet(SECRET_KEY)

import os
from cryptography.fernet import Fernet

# Retrieve the key from the environment variable or generate a new one
SECRET_KEY = os.environ.get('SECRET_KEY')

if not SECRET_KEY:
    # Generate a new key if no key is found
    generated_key = Fernet.generate_key()
    
    # Convert the generated key to a string
    SECRET_KEY = generated_key.decode()

    # Store the key securely (e.g., in environment variables)
    os.environ['SECRET_KEY'] = SECRET_KEY

# Initialize Fernet with the secret key
fernet = Fernet(SECRET_KEY)