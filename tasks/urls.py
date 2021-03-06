from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .viewsets import TaskViewSet


app_name = 'tasks'

router = DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]

