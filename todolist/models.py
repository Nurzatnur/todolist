from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
