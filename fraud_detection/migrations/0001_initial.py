# Generated by Django 3.2.7 on 2021-09-08 13:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.CharField(max_length=16)),
                ('card_serial', models.CharField(max_length=10)),
                ('amount', models.CharField(max_length=999)),
                ('issued_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, default=datetime.datetime(2021, 9, 8, 13, 36, 15, 101302, tzinfo=utc))),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=50)),
                ('completed', models.BooleanField(default=False, null=True)),
                ('card', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_card', to='fraud_detection.card')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=9999)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='fraud_detection.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='fraud_detection.SecurityQuestion'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
