from rest_framework import serializers
from .models import Child, Task

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'name', 'streak']  
        #read_only_fields = ['streak']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'child', 'description', 'completed']

