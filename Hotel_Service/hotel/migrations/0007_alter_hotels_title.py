# Generated by Django 3.2 on 2021-06-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_hotels_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]