from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Task


class TaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['url', 'description', 'owner']
        # override default view_name format from `{model}-detail` to `{app_name}:{model}-detail`
        # https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
        extra_kwargs = {
            'url': {'view_name': 'tasks:task-detail'},
            'owner': {'view_name': 'users:user-detail'},
        }
