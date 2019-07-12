from django.contrib.gis import admin
from .models import Station
from leaflet.admin import LeafletGeoAdmin


class StationAdmin(LeafletGeoAdmin):
    list_display = ('station_name', 'station_point', 'station_date_retrieved')


admin.site.register(Station, StationAdmin)

