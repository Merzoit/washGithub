# Generated by Django 4.0.3 on 2022-05-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_blank_chairs_blank_dc_ceiling_blank_dc_floor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blank',
            name='date',
        ),
        migrations.AddField(
            model_name='blank',
            name='date',
            field=models.ManyToManyField(blank=True, db_column='date', null=True, to='core.date', verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='blank',
            name='dry_clining',
            field=models.BooleanField(default=False, verbose_name='Химчистка'),
        ),
    ]
