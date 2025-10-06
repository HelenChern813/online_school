from rest_framework.serializers import ModelSerializer

from education.serializers import PaymentSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор модели пользователя"""

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["email", "phone", "avatar", "city", "payments"]
