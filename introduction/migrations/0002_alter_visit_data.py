# Generated by Django 5.1.2 on 2024-11-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='data',
            field=models.JSONField(default=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ),
    ]
