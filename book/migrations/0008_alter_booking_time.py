# Generated by Django 5.1.5 on 2025-02-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_booking_date_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(unique=True),
        ),
    ]
