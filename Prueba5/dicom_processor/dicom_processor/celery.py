from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configura el entorno de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dicom_processor.settings')

app = Celery('dicom_processor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()