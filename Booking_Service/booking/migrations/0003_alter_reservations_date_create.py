# Generated by Django 3.2 on 2021-06-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_reservations_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='date_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
