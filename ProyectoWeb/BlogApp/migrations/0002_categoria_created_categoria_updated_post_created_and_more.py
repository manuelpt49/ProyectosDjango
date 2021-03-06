# Generated by Django 4.0 on 2022-01-03 16:13

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 1, 3, 16, 12, 48, 790362, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
