import django

__version__ = '3.10.0rc2'

if django.VERSION < (3, 2):
    default_app_config = 'cms.apps.CMSConfig'
