from django.shortcuts import render
from .models import Station
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.views.generic import ListView, CreateView
import random, requests as req, json


# Not Use This Anymore
def index(request):

    context = {
        'stations': Station.objects.all()
    }

    return render(request, 'weatherstation/index.html', context)


# Home View
class StationListView(ListView):
    model = Station
    template_name = 'weatherstation/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'stations'


class ChartListView(ListView):
    model = Station
    template_name = 'weatherstation/charts.html'
    context_object_name = 'stations'


class StationCreateView(CreateView):
    model = Station
    fields = ['station_name', 'station_temperature', 'station_humidity', 'station_ambient_light', 'station_pressure',
              'station_altitude', 'station_point', 'station_date_retrieved']


def about(request):
    from .store_Sensor_Data_to_DB import sensor_data_handler
    sensor_data_handler("Test MQTT About Dummy", "Dummy message About Page")
    context = {
        'title': 'About',
    }

    return render(request, 'weatherstation/about.html', context)


def add_station(request):
    context = {
        'title': 'Add Station',
    }

    return render(request, 'weatherstation/add_station.html', context)


def add_station_form_submission(request):
    station_name = str(request.POST["station_name"])
    station_temperature = float(request.POST["station_temperature"])
    station_humidity = float(request.POST["station_humidity"])
    station_ambient_light = int(request.POST["station_ambient_light"])
    station_pressure = float(request.POST["station_pressure"])
    station_altitude = float(request.POST["station_altitude"])
    station_point = Point(13.72, 100.77)
    station_pm25 = random.randrange(100)
    station_date_retrieved = timezone.now()

    station = Station(station_name=station_name,station_temperature=station_temperature,station_humidity=station_humidity,
                      station_ambient_light=station_ambient_light,station_pressure=station_pressure,station_altitude=station_altitude,
                      station_point=station_point,station_pm25=station_pm25,station_date_retrieved=station_date_retrieved)
    station.save()

    context = {
        'title': 'Add Station',
    }

    return render(request, 'weatherstation/add_station_form_submission.html', context)
