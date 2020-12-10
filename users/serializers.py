from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from django.contrib.auth.models import User

from tasks.serializers import TaskSerializer

class UserSerializer(HyperlinkedModelSerializer):
    
    # NOTE: HyperlinkedRelatedField and TaskSerializer replaced by extra_kwargs
    # tasks = HyperlinkedRelatedField(view_name='tasks:task-detail', read_only=True, many=True)
    # tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tasks']
        # override default view_name format from `{model}-detail` to `{app_name}:{model}-detail`
        # https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail'},
            'tasks': {'view_name': 'tasks:task-detail'},
        }
