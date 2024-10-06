from attr.validators import max_len
from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return self.name