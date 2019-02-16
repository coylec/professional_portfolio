from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_URL = 'http://127.0.0.1:8000'

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')


SECURE_SSL_REDIRECT = False