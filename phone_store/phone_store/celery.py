import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phone_store.settings')

app = Celery('phone_store', )
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
