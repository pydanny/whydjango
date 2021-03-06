import os
import sys
import site

from os.path import abspath, dirname, join
from site import addsitedir

# Virtualenv env is at the same level as the repo directory
site_packages = '/home/whydjango/whydjango-env/lib/python2.6/site-packages/'
site.addsitedir(os.path.abspath(site_packages))

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "whydjango.settings"

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
