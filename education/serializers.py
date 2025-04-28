from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from education.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
