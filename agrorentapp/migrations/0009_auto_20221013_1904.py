# Generated by Django 3.0.14 on 2022-10-13 13:34

import agrorentapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrorentapp', '0008_auto_20221006_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='tool_photo',
            field=models.ImageField(upload_to=agrorentapp.models.PathRename('images')),
        ),
    ]
