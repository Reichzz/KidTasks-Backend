from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=100)
    streak = models.IntegerField(default=0) 

    def __str__(self):
        return self.name


class Task(models.Model):
    child = models.ForeignKey('Child', related_name='tasks', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
      
      
