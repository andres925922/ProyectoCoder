# Generated by Django 4.0.5 on 2022-07-26 21:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0005_remove_message_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='room',
            name='messages',
            field=models.ManyToManyField(related_name='messages', to='Users.message'),
        ),
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]