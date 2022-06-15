import environ

from book.book.settings.base import *

env = environ.ENV()

DEBUG = env.bool("DEBUG", False)

SECRETY_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {"default": env.db()}
