from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=60)
    creation_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
      
      #Noc
