"""
ASGI config for website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from socket import gethostbyname, gethostname

from django.core.asgi import get_asgi_application

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

application = get_asgi_application()
