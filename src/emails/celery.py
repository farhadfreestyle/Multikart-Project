from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTING_MODULE' , 'multikart.settings')

app = Celery ('multikart')

app.config_from_object('django.conf:settings' , namespace='CELERY')

app.conf.broker_url = 'redis://localhost:6379/0'

app.conf.beat_schedule = {
    "every menth": {
        "task": "emails.tasks.monthly_email_sender",
        'schedule': crontab(0, 0, day_of_month='1'),
    }
}

app.autodiscover_tasks()