# Generated by Django 3.0.14 on 2022-10-30 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrorentapp', '0010_auto_20221029_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='request_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 30, 14, 43, 58)),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 30, 14, 43, 58)),
        ),
    ]
