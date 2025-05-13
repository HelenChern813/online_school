from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer

from education.models import Course, Lesson, Payment, UpdateSubscriptionCourse
from education.validators import validate_valid_link


class CourseSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    def get_lessons(self, obj):
        name_lesson = []
        for i in obj.lesson_set.all():
            name_lesson.append(i.name)
        return name_lesson

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    video = CharField(validators=[validate_valid_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
