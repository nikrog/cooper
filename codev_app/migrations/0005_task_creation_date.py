# Generated by Django 2.1.7 on 2019-03-03 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0004_auto_20190303_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]