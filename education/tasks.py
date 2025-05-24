from celery import shared_task
from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from education.models import Course


@shared_task
def sending_messages_to_users(course_id):
    """Асинхронная рассылка писем пользователям об обновлении материалов курса"""

    course = Course.objects.get(id=course_id)
    subscriptions = course.course_subscription.all()
    recipient_emails = [subscription.user.email for subscription in subscriptions]

    subject = f'Обновление курса: {course.name}'
    message = f'Курс "{course.name}" был обновлен. Проверьте новые материалы!'
    from_email = DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, recipient_emails)
