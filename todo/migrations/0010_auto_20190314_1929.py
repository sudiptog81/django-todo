# Generated by Django 2.1.7 on 2019-03-14 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20190314_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 19, 29, 10, 478160)),
        ),
    ]