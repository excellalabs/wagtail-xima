from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'django_nose',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!@uqrj1=0riqnmyl+79jbsu5t$uz7=7rjc1+sx=1(%)o4ox6c'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
