from urllib.parse import urlparse
from rest_framework.serializers import ValidationError


def validate_valid_link(value: str) -> None:
    parsed_url = urlparse(value)
    if parsed_url.scheme != 'https' or parsed_url.netloc != 'www.youtube.com' :
        raise ValidationError("Использован неккоректный ресурс для источника видео")
