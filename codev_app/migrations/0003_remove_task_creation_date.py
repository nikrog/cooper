# Generated by Django 2.1.7 on 2019-03-03 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0002_auto_20190224_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='creation_date',
        ),
    ]
