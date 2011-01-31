DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ( ('Minh Tran', 'mtgred@gmail.com'),)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'colons.db',   # Or path to database file if using sqlite3.
        'USER': '',            # Not used with sqlite3.
        'PASSWORD': '',        # Not used with sqlite3.
        'HOST': '',            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',            # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Brussels'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin'

SECRET_KEY = '#ob3v7(blqd1sg4!f4wo@zvef&5gqh6*9s^5n5choak1f__3dl'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'colons.urls'
TEMPLATE_DIRS = ('templates')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'colons.ranking',
)
