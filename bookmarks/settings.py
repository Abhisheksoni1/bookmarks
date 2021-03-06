"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.core.urlresolvers import reverse_lazy

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l&9@0q%05kue)rfee2s@i41x_(3@vy1pn)%h8lex10f*7vf3$@'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
ALLOWED_HOSTS = []
# for social authentication
SOCIAL_AUTH_FACEBOOK_KEY = '1070590949655296'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'f9b77a0168eef8c2ed9f183d8277dfbc'  # Facebook App Secret

SOCIAL_AUTH_TWITTER_KEY = ' tEtkA4mSH3NPKOp6pNumlYeOx'  # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'AxcY4bEzGxElSGsS0bO7YEqTEt2Wcz3dLydHh2yMdONB8Q27JP'  # Twitter Consumer Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ' 648962815028-s9fsccjm5o8n9be3qq02i1s89qj1cstb.apps.googleusercontent.com'  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'wfOyN89YBfUfVnI7Diq71m1t'  # Google Consumer Secret
ABSOLUTE_URL_OVERRIDES = {'auth.user': lambda u: reverse_lazy('user_detail',
                                                              args=[u.username])}
THUMBNAIL_DEBUG = True
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
)
# Application definition

INSTALLED_APPS = (
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'social.apps.django_app.default',
    'images',
    'sorl.thumbnail',
    'actions',
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

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
