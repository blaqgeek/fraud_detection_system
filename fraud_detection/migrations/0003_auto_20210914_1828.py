# Generated by Django 3.2.7 on 2021-09-14 18:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fraud_detection', '0002_auto_20210908_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=19),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 14, 18, 28, 39, 285369, tzinfo=utc)),
        ),
    ]
