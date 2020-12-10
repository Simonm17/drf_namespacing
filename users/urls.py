from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .viewsets import UserViewSet


router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]