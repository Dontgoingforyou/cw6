from django.db import models

from users.models import User


class Message(models.Model):
    topic = models.CharField(max_length=200, verbose_name="Тема")
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.topic
