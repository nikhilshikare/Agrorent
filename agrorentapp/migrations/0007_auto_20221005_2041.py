# Generated by Django 3.0.14 on 2022-10-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrorentapp', '0006_auto_20221005_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='tool_photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
