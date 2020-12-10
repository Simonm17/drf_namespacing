from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    tasks = HyperlinkedRelatedField(view_name='task-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tasks']