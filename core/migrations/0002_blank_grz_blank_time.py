# Generated by Django 4.0.4 on 2022-04-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blank',
            name='grz',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='ГРЗ автомобиля'),
        ),
        migrations.AddField(
            model_name='blank',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
