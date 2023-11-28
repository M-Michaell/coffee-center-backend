from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_end.settings')

app = Celery('back_end')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'cancel-old-orders': {
        'task': 'order.tasks.cancel_old_orders',  
        # 'schedule': crontab(hour=0, minute=0), 
        'schedule': crontab(minute='*'),

    },
}

app.autodiscover_tasks()