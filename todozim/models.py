from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ListOfTasks(models.Model):
    title = models.CharField(max_length=80)
    createAt = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)

class Task(models.Model):
    description = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    listTasks = models.ForeignKey(ListOfTasks, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.description)