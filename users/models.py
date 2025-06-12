from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите свою почту")
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон", help_text="Укажите свой телефон"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Укажите свой город")
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар", help_text="Загрузите изображение"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]
