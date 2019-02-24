# Generated by Django 2.1.7 on 2019-02-24 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='pokemons.png', upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=10000)),
                ('creation_date', models.DateTimeField()),
                ('author', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codev_app.Image')),
            ],
        ),
    ]
