from .models import Stations, StationLogs
from django.utils import timezone
from django.contrib.gis.geos import Point
import json


# ===============================================================
# Functions to push Sensor Data Log into Database
def sensor_data_handler(msg):
    # Fetch data from JSON message
    station_data = json.loads(msg)

    station_id = int(station_data['station_id'])
    temperature = float(station_data['temperature'])
    humidity = float(station_data['humidity'])
    pm10 = int(station_data['pm10'])
    pm25 = int(station_data['pm25'])
    latitude = float(station_data['latitude'])
    longitude = float(station_data['longitude'])
    point = Point(longitude, latitude)
    timestamp = timezone.localtime(timezone.now())

    new_log = StationLogs(station_temperature=temperature, station_humidity=humidity,
                          station_pm10=pm10, station_pm25=pm25, station_pm1=0,
                          station_latitude=latitude, station_longitude=longitude, station_point=point,
                          station_recorded_time=timestamp, station_id=station_id)

    # Push new log into Database Table
    new_log.save(force_insert=True)

    # # Update Station Object of the log
    # station = Stations.objects.get(station_id=station_id)
    # station.battery_level = 100
    #
    # # Save into Database Table
    # station.save()


# ===============================================================
# Functions to Update Station Battery Level into Database
def sensor_data_handler_update(topic, msg):

    # Fetch data from JSON message
    station_data = json.loads(msg)
    station_id = station_data['station_id']
    battery_level = station_data['battery_level']

    # Get Station data from Database
    update_station = Stations.objects.get(station_id=station_id)

    #  Update Station Data
    update_station.battery_level = battery_level

    # Save into Database Table
    update_station.save()


