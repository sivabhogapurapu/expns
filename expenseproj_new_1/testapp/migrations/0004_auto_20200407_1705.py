# Generated by Django 3.0 on 2020-04-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20200406_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=30)),
                ('creationdate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='expenses',
            name='paidby',
            field=models.CharField(max_length=64),
        ),
    ]
