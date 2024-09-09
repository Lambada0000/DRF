from django.urls import path
from rest_framework.routers import SimpleRouter

from Ims.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonRetrieveAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)
from Ims.apps import ImsConfig

app_name = ImsConfig.name

router = SimpleRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lessons_delete"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
]

urlpatterns += router.urls
