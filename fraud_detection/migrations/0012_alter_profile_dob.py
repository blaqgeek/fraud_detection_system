# Generated by Django 3.2.7 on 2021-09-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud_detection', '0011_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
    ]
