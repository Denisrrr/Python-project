# Generated by Django 4.1.5 on 2023-01-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='header_bg',
            field=models.ImageField(blank=True, null=True, upload_to='images/main', verbose_name='Изображение-фон для шапки'),
        ),
    ]