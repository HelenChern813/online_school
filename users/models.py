from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import Course


class User(AbstractUser):
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


class Payment(models.Model):
    CASH = "cash"
    ONLINE_PAYMENT = "online_payment"

    STATUS_PAYMENT = [
        (CASH, "Наличные"),
        (ONLINE_PAYMENT, "Перевод на счет"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
    date_pay = models.DateTimeField(verbose_name="Дата и время оплаты")
    content_pay = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=15,
        choices=STATUS_PAYMENT,
        default=ONLINE_PAYMENT,
        verbose_name="Способ оплаты",
    )
