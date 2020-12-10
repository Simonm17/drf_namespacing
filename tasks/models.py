from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    description = models.CharField(max_length=250, blank=True)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}, {self.description}'