# Generated by Django 3.1.2 on 2020-10-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUsApp', '0002_auto_20201008_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='PhoneNumber',
            field=models.BigIntegerField(blank=True),
        ),
    ]
