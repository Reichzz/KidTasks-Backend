from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Child, Task
from .serializers import ChildSerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    @action(detail=True, methods=['post'], url_path='reset-streak')
    def reset_streak(self, request, pk=None):
        child = self.get_object()
        child.streak = 0  # Reinicia la racha
        child.save()
        return Response({'status': 'streak reset'}, status=status.HTTP_200_OK)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = self.queryset
        child_id = self.request.query_params.get('child_id')
        if child_id is not None:
            queryset = queryset.filter(child__id=child_id)
        return queryset