from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=60)
    creation_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    consecutive_days = models.IntegerField(default=0)

    def __str__(self):
        return self.description
