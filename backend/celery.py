from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-tasks-daily': {
        'task': 'kidtasks.tasks.check_tasks_and_update_streaks',  # Reemplaza 'kidtasks' si el nombre de tu app es diferente
        'schedule': crontab(hour=23, minute=59),  # Ejecuta la tarea a las 23:59 todos los días
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')