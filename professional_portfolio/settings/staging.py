from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')


SECURE_SSL_REDIRECT = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}