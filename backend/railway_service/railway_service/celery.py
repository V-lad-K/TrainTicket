import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'railway_service.settings')

# app = Celery('user_service', broker='redis://localhost:6379')
app = Celery('railway_service', )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
