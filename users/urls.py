from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .viewsets import UserViewSet


app_name = 'users'

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

