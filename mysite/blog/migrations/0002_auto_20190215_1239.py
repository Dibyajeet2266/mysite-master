# Generated by Django 2.1.5 on 2019-02-15 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 12, 39, 24, 499841, tzinfo=utc), verbose_name='date_joined'),
        ),
    ]
