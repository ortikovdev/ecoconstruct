# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2757461/data/www/ecoconstruct.uz/base')
sys.path.insert(1, '/var/www/u2757461/data/venvlist/ecoconstructvenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'base.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

