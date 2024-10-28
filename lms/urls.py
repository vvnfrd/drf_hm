from django.urls import path
from rest_framework.routers import DefaultRouter
from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-llist'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-info'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/destroy/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-destroy')
] + router.urls