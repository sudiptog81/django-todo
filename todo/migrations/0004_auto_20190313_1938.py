# Generated by Django 2.1.4 on 2019-03-13 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190313_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 19, 38, 59, 101117)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='todo_completed',
            field=models.BooleanField(default=False),
        ),
    ]