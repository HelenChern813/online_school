from django.urls import path
from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig
from education.views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView, PaymentListView,
                             UpdateSubscriptionCourseAPIView)

app_name = EducationConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("users_list/", PaymentListView.as_view(), name="user_list"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("course/<int:course_id>/subscribe/", UpdateSubscriptionCourseAPIView.as_view(), name="subscribe_on_course"),
] + router.urls
