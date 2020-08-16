# Generated by Django 3.0.8 on 2020-08-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_review_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]