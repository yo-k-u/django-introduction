# Generated by Django 5.1.2 on 2024-11-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0002_alter_visit_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='data',
            field=models.JSONField(),
        ),
    ]
