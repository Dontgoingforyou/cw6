from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(**NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True)

    class Meta:
        verbose_name = "Клиент сервиса"
        verbose_name_plural = "Клиенты сервиса"

    def __str__(self):
        return f"{self.full_name} ({self.email})"
