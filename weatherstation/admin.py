from django.contrib.gis import admin
from .models import Stations, StationLogs
from leaflet.admin import LeafletGeoAdmin


class StationAdmin(LeafletGeoAdmin):
    list_display = ('station_id', 'description')


class StationLogAdmin(LeafletGeoAdmin):
    list_display = ('station_id', 'log_id', 'station_temperature', 'station_recorded_time')


admin.site.register(Stations, StationAdmin)
admin.site.register(StationLogs, StationLogAdmin)
