# Generated by Django 4.0.5 on 2022-07-28 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.RemoveField(
            model_name='about',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='about',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='about',
            name='tel',
        ),
    ]
