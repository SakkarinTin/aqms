from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as geomodels
from django.db.models import Manager as GeoManager


class Station(models.Model):
    station_name = models.CharField(max_length=40)
    station_temperature = models.DecimalField(max_digits=10, decimal_places=4)
    station_humidity = models.DecimalField(max_digits=10, decimal_places=4)
    station_ambient_light = models.IntegerField()
    station_pressure = models.DecimalField(max_digits=10, decimal_places=4)
    station_altitude = models.DecimalField(max_digits=10, decimal_places=4)
    station_point = geomodels.PointField(srid=4326)
    station_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    station_longitude = models.DecimalField(max_digits=10, decimal_places=6)
    station_date_retrieved = models.DateTimeField(default=timezone.now)
    objects = GeoManager()

    def save(self, *args, **kwargs):
        self.station_latitude = self.station_point.x
        self.station_longitude = self.station_point.y
        super(Station, self).save(*args, **kwargs)

    def __str__(self):
        return self.station_name

