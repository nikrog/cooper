# Generated by Django 2.1.7 on 2019-03-03 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0005_task_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
