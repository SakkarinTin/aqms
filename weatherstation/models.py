from django.utils import timezone
from django.db import models
from django.contrib.gis.db import models as geomodels
from django.db.models import Manager as GeoManager


class Stations(models.Model):
    station_id = models.AutoField(primary_key=True)
    description = models.TextField()
    battery_level = models.IntegerField()

    def get_fields_and_values(self):
            return [(field, field.value_to_string(self)) for field in Stations._meta.fields]

    def __str__(self):
        return str(self.station_id)

    class Meta:
        ordering = ['station_id']
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'


class StationLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(Stations, related_name="logs", on_delete=models.CASCADE)
    station_temperature = models.DecimalField(max_digits=10, decimal_places=2)
    station_humidity = models.DecimalField(max_digits=10, decimal_places=2)
    station_pm25 = models.IntegerField()
    station_pm10 = models.IntegerField()
    station_pm1 = models.IntegerField()
    station_point = geomodels.PointField(srid=4326)
    station_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    station_longitude = models.DecimalField(max_digits=10, decimal_places=6)
    station_recorded_time = models.DateTimeField(default=timezone.now)
    objects = GeoManager()

    def get_fields_and_values(self):
            return [(field, field.value_to_string(self)) for field in StationLogs._meta.fields]

    def save(self, *args, **kwargs):
        self.station_latitude = self.station_point.y
        self.station_longitude = self.station_point.x
        super(StationLogs, self).save(*args, **kwargs)

    def __str__(self):
        return "Log: " + str(self.log_id) + " of Station: " + str(self.station)

    class Meta:
        ordering = ['log_id', '-station_recorded_time']
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
