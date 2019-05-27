from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Station(models.Model):
    title = models.CharField(max_length=50)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    ambient_light = models.IntegerField()
    pressure = models.FloatField(default=0)
    altitude = models.FloatField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



