# Generated by Django 5.1.5 on 2025-02-10 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_options_about_about_barber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_barber',
        ),
    ]
