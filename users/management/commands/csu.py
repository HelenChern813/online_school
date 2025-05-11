from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@exemple.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("123qwe")
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Успешно создан суперпользователь {user.email}"))
