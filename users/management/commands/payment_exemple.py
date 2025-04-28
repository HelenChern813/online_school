from django.core.management.base import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    """Кастомная команда создания платежа"""

    def handle(self, *args, **options):
        pay = Payment.objects.create(user=1, content_pay=1, payment_amount=150000)
        pay.save()
        self.stdout.write(self.style.SUCCESS(f"Успешно создан пример платежа {pay.id}"))
