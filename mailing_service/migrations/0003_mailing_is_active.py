# Generated by Django 5.1.2 on 2024-11-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0002_client_owner_mailing_owner_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
