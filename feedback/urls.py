from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FeedbackViewSet, RegisterView, SurveyViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]