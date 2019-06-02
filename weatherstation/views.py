from django.http import HttpResponse
from django.shortcuts import render
from .models import Station
from django.utils import timezone
from django.contrib.gis.geos import GEOSGeometry


def index(request):
    context = {
        'station': 'station'
        # 'stations': Station.objects.all()
    }
    return render(request, 'weatherstation/index.html', context)


def about(request):
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
    station_title = str(request.POST["station_title"])
    station_temperature = float(request.POST["station_temperature"])
    station_humidity = float(request.POST["station_humidity"])
    station_ambient_light = int(request.POST["station_ambient_light"])
    station_pressure = float(request.POST["station_pressure"])
    station_altitude = float(request.POST["station_altitude"])
    station_location = GEOSGeometry('POINT(5 23)')
    station_date_retrieved = timezone.now()

    station = Station(station_title=station_title,station_temperature=station_temperature,station_humidity=station_humidity,
                      station_ambient_light=station_ambient_light,station_pressure=station_pressure,station_altitude=station_altitude,
                      station_location=station_location,station_date_retrieved=station_date_retrieved)
    station.save()

    context = {
        'title': 'Add Station',
    }

    return render(request, 'weatherstation/add_station_form_submission.html', context)
