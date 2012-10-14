import os.path
PROJECT_DIR = os.path.dirname(__file__)

# Import the installation specific settings
from djangoappengine.settings_base import *
from extra_settings import *

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

TEMPLATE_DEBUG = DEBUG

DATABASES = {}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!8j$ddza5$hrmg&3tw#$!pk-4$43zz!m@&(7*#y#*h&wfivkq='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',    
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates')    
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'djangoappengine',              
    'djangotoolbox',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',              

    'test',
)

ROOT_URLCONF ='urls'

# These next settings don't have any value right now, since the static file
# management is done thru the ``app.yaml`` file.
# If we wanted to use the Django admin interface, we would need these settings,
# in order to run ``collectstatic`` and collect the admin static assets in one
# folder.
# STATIC_URL = 'static'
# STATIC_ROOT = 'static'
# Pick up the static files from the ``static/`` folder, and place them under the ``STATIC_ROOT``
STATICFILES_DIRS =  (
# CSS and static files, in 'static' folder
	os.path.join(PROJECT_DIR, STATIC_ROOT),
)                            
# URL prefix for admin media
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

