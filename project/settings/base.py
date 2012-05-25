# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *
import os

# Path from the project
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', x)

# Name of the top-level module where you put all your apps.
# If you did not install Playdoh with the funfactory installer script
# you may need to edit this value. See the docs about installing from a
# clone.
PROJECT_MODULE = 'project'

# Defines the views served for root URLs.
ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

INSTALLED_APPS = (
    'funfactory',
    'jingo_minify',
    'tower',
    'cronjobs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'commonware.response.cookies',
    'djcelery',
    'django_nose',
    'session_csrf',
    'product_details',
    'django.contrib.admin',

    # 3rd party
    'ajax_select',
    'django_browserid',
    'django_extensions',


    # Application base, containing global templates.
    '%s.base' % PROJECT_MODULE,
    '%s.taskboard' % PROJECT_MODULE,
    'compressor',
)


# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
    'debug_toolbar',
]

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS['messages'] = [
    ('%s/**.py' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_python'),
    ('%s/**/templates/**.html' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_template'),
    ('templates/**.html',
        'tower.management.commands.extract.extract_tower_template'),
],

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable JS files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))


ES_DISABLED = True
ES_HOSTS = ['127.0.0.1:9200']
ES_INDEXES = dict(default='taskboard')


# Static and Media
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    )

STATICFILES_DIRS = (
    here('static/'),
    )
STATIC_URL = r'/static/'

MEDIA_URL = r'media'

# Templates
TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

TEMPLATE_DIRS = here('templates')

JINJA_CONFIG = {
    'extensions': [
    'tower.template.i18n',
    'jinja2.ext.do',
    'jinja2.ext.with_',
    'jinja2.ext.loopcontrols',
    'compressor.contrib.jinja2ext.CompressorExtension',
    ]
}

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
    )

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.static',
    'django_browserid.context_processors.browserid_form',
    )
