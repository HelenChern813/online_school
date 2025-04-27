from django.db import models


class Course(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]


class Lesson(models.Model):
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
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Курс"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]
