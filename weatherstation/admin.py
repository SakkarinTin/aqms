from django.contrib.gis import admin
from .models import Station
from leaflet.admin import LeafletGeoAdmin

class StationAdmin(LeafletGeoAdmin):
    list_display = ('station_title', 'station_location')


admin.site.register(Station, StationAdmin)
# admin.site.register(Station, admin.GeoModelAdmin)

