import datetime

from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField('date created')
    author = models.CharField(max_length=200)

    def was_created_3_months_ago(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=90)

    def rude_task(self):
        words = ['fuck', 'shit', 'asshole']
        return any(w.lower() in self.content for w in words)


