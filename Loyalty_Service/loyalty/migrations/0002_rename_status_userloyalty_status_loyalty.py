# Generated by Django 3.2 on 2021-06-23 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userloyalty',
            old_name='status',
            new_name='status_loyalty',
        ),
    ]
