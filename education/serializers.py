from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer

from education.models import Course, Lesson, Payment, UpdateSubscriptionCourse
from education.validators import validate_valid_link


class CourseSerializer(ModelSerializer):
    """Сериализатор модели курса"""

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
    """Сериализатор модели урока"""

    video = CharField(validators=[validate_valid_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Сериализатор модели платежа с реализацией валидации"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ("date_pay", "payment_amount", "payment_method", "session_id", "link_pay")

    def validate(self, data):

        course = data.get("course")
        lesson = data.get("lesson")

        if course and lesson:
            raise serializers.ValidationError("Нужно указать урок или курс.")
        if not course and not lesson:
            raise serializers.ValidationError("Необходимо обязательно указать урок или курс.")

        return data
