from django.http import HttpResponse
from django.shortcuts import render
from .models import Station

stations = [
    {
        'title': 'Station 1',
        'temperature': 37,
        'humidity': 22,
        'ambient_light': 120,
        'pressure': 12,
        'altitude': 5,
        'date_posted': 'May 21, 2019'
    },
    {
        'title': 'Station 2',
        'temperature': 34,
        'humidity': 19,
        'ambient_light': 5,
        'pressure': 9,
        'altitude': 20,
        'date_posted': 'May 22, 2019'
    }
]

def index(request):
    context = {
        # 'stations': Station.objects.all()
        'stations': stations
    }
    return render(request, 'weatherstation/index.html', context)

def about(request):
    return render(request, 'weatherstation/about.html', {'title': 'About'})
