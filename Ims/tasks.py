from celery import shared_task
from django.core.mail import send_mail
from config import settings
from Ims.models import Subscription


@shared_task
def start_mailshot(course):
    """Отправляет сообщения пользователям с подпиской об обновлениях материалов курса."""
    course_updates = Subscription.objects.filter(course=course.id)
    for single_update in course_updates:
        send_mail(
            subject='Обновление материалов курса!',
            message=f'Вышло обновление материалов курса - {single_update.course.title}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[single_update.user.email]
        )
    print("start_mailshot: TRUE")
    