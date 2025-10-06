from django.conf import settings
from django.db import models

from users.models import User


class Course(models.Model):
    """Модель курса обучения"""

    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.CharField(max_length=250, verbose_name="Описание", help_text="Введите описание курса")
    photo = models.ImageField(
        upload_to="education/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите превью курса",
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец", help_text="Укажите владельца"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]


class Lesson(models.Model):
    """Модель урока обучения"""

    name = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.CharField(max_length=250, verbose_name="Описание", help_text="Введите описание урока")
    photo = models.ImageField(
        upload_to="education/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите превью урока",
    )
    video = models.TextField(verbose_name="Ссылка на видео", help_text="Вставьте ссылку на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Курс")
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец", help_text="Укажите владельца"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]


class Payment(models.Model):
    CASH = "cash"
    ONLINE_PAYMENT = "online_payment"

    STATUS_PAYMENT = [
        (CASH, "Наличные"),
        (ONLINE_PAYMENT, "Перевод на счет"),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Пользователь")
    date_pay = models.DateTimeField(verbose_name="Дата и время оплаты")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Оплаченный курс")
    payment_amount = models.IntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=15,
        choices=STATUS_PAYMENT,
        default=ONLINE_PAYMENT,
        verbose_name="Способ оплаты",
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Оплаченый урок")
    session_id = models.CharField(max_length=300, blank=True, null=True, verbose_name="Сессия")
    link_pay = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на платеж")

    def __str__(self):
        return f"Платеж {self.session_id} на сумму {self.payment_amount} от {self.user}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class UpdateSubscriptionCourse(models.Model):
    """Модел на проверку подписки"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_subscriptions",
        verbose_name="Пользователь",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_subscriptions", verbose_name="Курс"
    )

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.name}"

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курсы"
