from rest_framework.serializers import ValidationError

valid_link = "https://www.youtube.com/"


def validate_valid_link(value):
    if valid_link not in value.lower():
        raise ValidationError("Использован неккоректный ресурс для источника видео")
