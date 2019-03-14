# Generated by Django 2.1.7 on 2019-03-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('todo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('todo_content', models.TextField()),
                ('todo_author', models.CharField(max_length=255)),
                ('todo_completed', models.BooleanField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]