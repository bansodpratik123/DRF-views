# Generated by Django 3.2.6 on 2022-03-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_alter_empdetails_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetails',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
