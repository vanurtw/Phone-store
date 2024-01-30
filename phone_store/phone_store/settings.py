"""
Django settings for phone_store project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-we9=$5wg4cftc^dnp1yef2da4^5e+k)$lespiwh&zy18urcsk('

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
    'store.apps.StoreConfig',
    'cart.apps.CartConfig',
    'wishlist.apps.WishlistConfig',
    'debug_toolbar',
    'users.apps.UsersConfig',
    'order.apps.OrderConfig',
    'payment.apps.PaymentConfig',
    'blog.apps.BlogConfig',
    'taggit',


]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'phone_store.urls'

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
                'store.context_processor.context_processor.cart_context',
                'store.context_processor.context_processor.wishlist_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'phone_store.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

INTERNAL_IPS = [
    "127.0.0.1",
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CART_SESSION_ID = 'cart'
WISHLIST_SESSION_ID = 'wishlist'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'phone_store.authentication.EmailBackend',
                           ]

EMAIL_HOST_USER = 'vanuartw@mail.ru'
EMAIL_HOST_PASSWORD = '1TJNJ3kpfPwetP6sqZqX'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672"

STRIPE_PUBLISHABLE_KEY = 'pk_test_51OHKGHA6Z3RPpTyQsp4ahqoTF2vQMnY90ywjOSXrKzmSHmekfpPnfI26W3bz1FZ6zCcqhLdv7BvXxneOJKIVGA5Z00wtubLqWg'
STRIPE_SECRET_KEY = 'sk_test_51OHKGHA6Z3RPpTyQAzUmFBOVC617HlB7beIop0S228G0twmVbmYpbEjtgz22rfHRfnYahVTYjh7dfcdtkZWlfXbo00ZWes5Ai4'
STRIPE_API_VERSION = '2022-08-01'
STRIPE_WEBHOOK_SECRET = 'whsec_7169049f08393468ac73e5b57f19404d5468c25e56b2216239f2c5a6f85ee8ce'
