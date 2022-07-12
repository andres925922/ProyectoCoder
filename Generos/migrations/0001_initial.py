# Generated by Django 4.0.5 on 2022-07-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modificated_at', models.DateField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('descripcion', models.CharField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
