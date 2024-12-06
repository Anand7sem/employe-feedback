from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]