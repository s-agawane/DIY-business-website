"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from socket import gethostbyname, gethostname

from django.core.wsgi import get_wsgi_application

ipaddress = gethostbyname(gethostname())
if ipaddress.startswith('127.0'):
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'website.settings.development'
    )
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'website.settings.production'
    )

application = get_wsgi_application()
