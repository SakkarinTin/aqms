from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Station(models.Model):
    station_title = models.CharField(max_length=100)
    station_temperature = models.FloatField(default=0)
    station_humidity = models.FloatField(default=0)
    station_ambient_light = models.IntegerField()
    station_pressure = models.FloatField(default=0)
    station_altitude = models.FloatField(default=0)
    station_latitude = models.FloatField(default=0)
    station_longitude = models.FloatField(default=0)
    station_date_retrieved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.station_title



