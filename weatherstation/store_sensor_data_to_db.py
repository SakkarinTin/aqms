from .models import Station
from django.utils import timezone
from django.contrib.gis.geos import Point
import json


# ===============================================================
# Functions to push Sensor Data into Database
def sensor_data_handler(topic, msg):
    # Fetch data from JSON message
    hexiwear_data = json.loads(msg)

    station_name = "Hexiwear Station"
    station_temperature = hexiwear_data['temperature']
    station_humidity = hexiwear_data['humidity']
    station_pressure = hexiwear_data['pressure']
    station_altitude = hexiwear_data['altitude']
    station_ambient_light = hexiwear_data['ambient_light']
    station_pm25 = hexiwear_data['pm25']
    latitude_value = hexiwear_data['latitude']
    longitude_value = hexiwear_data['longitude']
    station_point = Point(longitude_value, latitude_value)
    station_date_retrieved = timezone.localtime(timezone.now())

    new_station = Station(station_name=station_name, station_temperature=station_temperature,
                      station_humidity=station_humidity,station_ambient_light=station_ambient_light,
                      station_pressure=station_pressure,station_altitude=station_altitude,
                      station_point=station_point, station_pm25=station_pm25, station_date_retrieved=station_date_retrieved)

    # Push new data into Database Table
    new_station.save()


# ===============================================================
# Functions to push Sensor Data into Database
def sensor_data_handler_update(topic, msg):
    # Get Station data from Database
    stations = Station.objects.all()
    updated_station = stations.get(id=1)

    # Fetch data from JSON message
    hexiwear_data = json.loads(msg)
    temperature_value = hexiwear_data['temperature']
    humidity_value = hexiwear_data['humidity']
    pressure_value = hexiwear_data['pressure']
    altitude_value = hexiwear_data['altitude']
    ambient_light_value = hexiwear_data['ambient_light']
    pm25_value = hexiwear_data['pm25']
    latitude_value = hexiwear_data['latitude']
    longitude_value = hexiwear_data['longitude']

    #  Update Station Data
    updated_station.station_name = "Hexiwear Station"
    updated_station.station_temperature = temperature_value
    updated_station.station_humidity = humidity_value
    updated_station.station_pressure = pressure_value
    updated_station.station_altitude = altitude_value
    updated_station.station_ambient_light = ambient_light_value
    updated_station.station_pm25 = pm25_value
    updated_station.station_point = Point(latitude_value, longitude_value)
    updated_station.station_date_retrieved = timezone.now()

    # Save into Database Table
    updated_station.save()


