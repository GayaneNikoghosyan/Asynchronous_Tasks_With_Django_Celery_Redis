# celery.py

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create a new Celery app.
app = Celery('myproject')

# Load the Django settings module.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and autodiscover tasks within your Django apps.
app.autodiscover_tasks()

