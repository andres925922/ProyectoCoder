# Generated by Django 4.0.5 on 2022-07-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_room_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='messages',
            field=models.ManyToManyField(to='Users.message'),
        ),
    ]
