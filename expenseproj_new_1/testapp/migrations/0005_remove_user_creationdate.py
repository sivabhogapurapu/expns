# Generated by Django 3.0 on 2020-04-07 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20200407_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='creationdate',
        ),
    ]
