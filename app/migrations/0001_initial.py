# Generated by Django 4.1.5 on 2023-01-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название профессии')),
                ('desc', models.TextField(verbose_name='Краткое описание')),
                ('where_used', models.TextField(verbose_name='Где востребована')),
                ('when_appeared', models.TextField(verbose_name='Когда появилась')),
                ('about_img', models.ImageField(blank=True, null=True, upload_to='images/main/', verbose_name='Изображение для раздела о профессии')),
                ('skills', models.TextField(verbose_name='Какие навыки необходимы для профессии')),
                ('skills_img', models.ImageField(blank=True, null=True, upload_to='images/main/', verbose_name='Изображение для раздела о навыках')),
                ('grades', models.TextField(verbose_name='Уровни по опыту работы')),
                ('how_to_become', models.TextField(verbose_name='Как войти в профессию')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
    ]