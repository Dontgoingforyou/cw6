from django.utils import timezone

from django.db import models

from clients.models import Client
from message.models import Message
from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Mailing(models.Model):
    """
    PERIODICITY_CHOICES, STATUS_CHOICES - наборы значении для полей periodicity и status соответственно
    """

    PERIODICITY_CHOICES = [
        ('once', 'Однократная'),
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_datetime = models.DateTimeField(default=timezone.now, verbose_name='Дата и время первой рассылки')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, default='once',
                                   verbose_name='Периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, related_name='mailings', verbose_name='Клиент сервиса')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('can_view_mailing', 'Can view mailing'),
            ('can_block_user', 'Can block user'),
            ('can_disable_mailing', 'Can disable mailing'),
        ]

    def __str__(self):
        return f"Рассылка: {self.start_datetime}, {self.periodicity}, {self.status}, {self.message}, {self.clients}"


class Attempt(models.Model):
    STATUS_CHOICES = [
        ('successful', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts', verbose_name='Попытка')
    attempt_datetime = models.DateTimeField(default=timezone.now,
                                            verbose_name='Дата и время попытки отправки рассылки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField(**NULLABLE)

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"

    def __str__(self):
        return f"Попытка: {self.mailing}, {self.attempt_datetime}, {self.status}, {self.server_response}"
