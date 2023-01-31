# Celery app

from celery import Celery

app = Celery('sistemaOmet')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


