# Generated by Django 4.0.1 on 2022-01-18 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
