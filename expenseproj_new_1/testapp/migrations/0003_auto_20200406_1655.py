# Generated by Django 3.0 on 2020-04-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200406_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='paidby',
            field=models.CharField(default='Sudheer', max_length=64),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='remarks',
            field=models.CharField(max_length=256),
        ),
    ]
