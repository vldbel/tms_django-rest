from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Book

@receiver(post_save, sender=Book)
def send_book_creation_notification(sender, instance, created, **kwargs):
    if created:  # Отправляем письмо только при создании новой записи
        subject = f'Новая книга добавлена: {instance.title}'
        message = (
            f'Новая книга была добавлена в базу данных:\n\n'
            f'Название: {instance.title}\n'
            f'Автор: {instance.author or "Не указан"}\n'
            f'Год: {instance.year}\n'
            f'Дата публикации: {instance.published_date}\n'
            f'Статус: {"Активна" if instance.is_active else "Неактивна"}'
        )
        from_email = 'vldbel@gmail.com'  # Укажите ваш Gmail
        recipient_list = ['vldbel@gmail.com']  # Кому отправлять (можно указать тот же email)

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,  # Если False, ошибки будут видны в консоли
        )
