# Generated by Django 4.0.1 on 2022-01-25 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='DNI',
        ),
    ]
