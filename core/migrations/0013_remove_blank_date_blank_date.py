# Generated by Django 4.0.3 on 2022-05-10 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_blank_date_blank_date_alter_blank_dry_clining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blank',
            name='date',
        ),
        migrations.AddField(
            model_name='blank',
            name='date',
            field=models.OneToOneField(blank=True, db_column='date', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.date', verbose_name='Дата'),
        ),
    ]