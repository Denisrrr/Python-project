# Generated by Django 4.1.5 on 2023-01-10 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_areastatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_img', models.ImageField(upload_to='images/salary/', verbose_name='Изображение графика востребованности')),
                ('table', models.TextField(verbose_name='Таблица статистики востребованности')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.profession', verbose_name='Выбранная профессия')),
            ],
            options={
                'verbose_name': 'Статистика по востребованности',
                'verbose_name_plural': 'Статистики по востребованности',
            },
        ),
    ]