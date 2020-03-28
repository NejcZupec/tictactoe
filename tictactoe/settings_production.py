from django.core.exceptions import ImproperlyConfigured

from .settings import *


def get_env_variable(var_name):
    """
    Get the environment variable or return exception.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the %s environment variable' % var_name
        raise ImproperlyConfigured(error_msg)


DEBUG = False

# TODO: temporarily disabled to test Heroku
# ALLOWED_HOSTS = ['tictactoe.zupec.net']

SECRET_KEY = get_env_variable('SECRET_KEY')

MIDDLEWARE_CLASSES += (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

# TODO: temporarily disabled to test Heroku
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': get_env_variable("DATABASE_NAME"),
#         'USER': get_env_variable("DATABASE_USER"),
#         'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
#         'HOST': get_env_variable("DATABASE_HOST"),
#         'PORT': '5432',
#     },
# }

