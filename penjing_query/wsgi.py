# coding: utf-8
"""
WSGI config for penjing_query project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

# 目前的问题是，不能通过django-admin runserver启动服务器。
# path = 'E:\\progdata2\\2018_06_penjing\\penjing_query'
# if path not in sys.path:
#   sys.path.append(path)
# sys.path.append(path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'penjing_query.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "penjing_query.settings")

application = get_wsgi_application()
