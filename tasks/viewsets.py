from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission already set by default in settings