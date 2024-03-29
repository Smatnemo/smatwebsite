"""
WSGI config for smatwebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os, sys, site

sys.path.append('/var/www/www.smatwebsite.co.uk/smatwebsite')
sys.path.append('/var/www/www.smatwebsite.co.uk/smatwebsite/smatwebsite')
sys.path.append('/var/www/www.smatwebsite.co.uk/smatwebsite/venv/lib/python3.10/site-packages')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smatwebsite.settings')

application = get_wsgi_application()
