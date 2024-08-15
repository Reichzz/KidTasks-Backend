from celery import shared_task
from django.utils import timezone
from .models import Child, Task

@shared_task
def check_tasks_and_update_streaks():
    children = Child.objects.all()
    for child in children:
        # Asumimos que quieres revisar las tareas del día anterior al correr la tarea después de la medianoche
        date_to_check = timezone.now().date() - timezone.timedelta(days=1)
        tasks = Task.objects.filter(child=child, date=date_to_check, completed=False)
        if not tasks.exists():
            child.streak += 1
            child.save()
        else:
            child.streak = 0  # Reiniciar la racha si alguna tarea no fue completada
            child.save()
