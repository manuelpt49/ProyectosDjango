# Generated by Django 4.0 on 2022-01-03 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_categoria_created_categoria_updated_post_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=models.TextField(default=datetime.datetime(2022, 1, 3, 16, 26, 39, 424533, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
