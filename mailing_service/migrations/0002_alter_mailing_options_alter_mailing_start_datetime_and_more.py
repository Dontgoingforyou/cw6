# Generated by Django 5.1.1 on 2024-09-30 15:03

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 30, 15, 3, 38, 903352, tzinfo=datetime.timezone.utc), verbose_name='Дата и время первой рассылки'),
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_datetime', models.DateTimeField(default=datetime.datetime(2024, 9, 30, 15, 3, 38, 904180, tzinfo=datetime.timezone.utc), verbose_name='Дата и время попытки отправки рассылки')),
                ('status', models.CharField(choices=[('successful', 'Успешно'), ('failed', 'Не успешно')], max_length=20)),
                ('server_response', models.TextField(blank=True, null=True)),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='mailing_service.mailing', verbose_name='Попытка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
