# Generated by Django 5.1.2 on 2024-10-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_data_dateevent_alter_data_timeframe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='tiсker',
            field=models.TextField(max_length=10),
        ),
    ]
