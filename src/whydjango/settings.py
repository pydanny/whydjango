# Django settings for whydjango project.
import os
import platform

PROJECT_ROOT = os.path.dirname(__file__)
PLATFORM_NODE = platform.node()


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Daniel Greenfeld', 'pydanny@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

USE_I18N = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, "media"))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, "static"))

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'd^5@ux-(-r7-*y791uwun(xq+h7p+=##9&jv#p627$eud!^6bd'

# List of callables that know how to import templates from various sources.
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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'whydjango.urls'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    )    
    
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)    

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.markup',
    'social_bookmarking',    
    'taggit',
    'south',
    'django_wysiwyg',
    'whydjango.books',    
    'whydjango.casestudies',
    'whydjango.core',    
)



TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',    
)

if DEBUG:
    
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    
    INSTALLED_APPS += ('debug_toolbar',)
    
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = { 
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': False,
    }    

try:
    
    from local_settings import *
except ImportError:
    pass