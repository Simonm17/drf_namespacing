from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ['url', 'description', 'owner']