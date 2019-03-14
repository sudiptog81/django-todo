from django.db import models
from datetime import datetime


class TodoItem(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo_content = models.TextField()
    todo_completed = models.BooleanField(default=False)
    todo_time = models.DateTimeField(default=datetime.now())
    date_created = models.DateTimeField(default=datetime.now())
