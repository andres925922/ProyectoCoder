# Generated by Django 4.0.5 on 2022-08-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discos', '0008_canciones_artista_canciones_artistas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discos',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='Discos'),
        ),
    ]