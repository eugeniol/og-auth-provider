"""
Django settings for oauth3 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2rm%x&zdvg7a@$l$qkbr_3=y#y7a##rug54yvxf2$m&u@++jxw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'oauth2_provider',
    'oauth2_provider_jwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'oauth2_provider.backends.OAuth2Backend',
)

SITE_ID = 1

ROOT_URLCONF = 'oauth3.urls'

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

WSGI_APPLICATION = 'oauth3.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ordergroove',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'ordergroove',
        'PASSWORD': 'sEcurez123',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

JWT_ISSUER = 'OneIssuer'

JWT_PRIVATE_KEY_RSA_ONEISSUER = """
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
"""

JWT_PAYLOAD_ENRICHER = 'oauth3.settings.payload_enricher'
JWT_ID_ATTRIBUTE = 'id'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


# myproject/myapp/jwt_utils.py

def payload_enricher(request):
    return {
        'sub': 'mysubject',
        # ...
    }
