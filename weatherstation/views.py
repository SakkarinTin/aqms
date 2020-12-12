from django.shortcuts import render
from .models import Stations, StationLogs
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.views.generic import ListView, CreateView
import random, requests as req, json
from django.http import JsonResponse
from .utils import serialize_bootstraptable

# Not Use This Anymore
def index(request):
    context = {
        'stationlogs': StationLogs.objects.all()
    }

    return render(request, 'weatherstation/index.html', context)


def charts(request):
    context = {
        'stationlogs': StationLogs.objects.all()
    }

    return render(request, 'weatherstation/charts.html', context)

    # data = StationLogs.objects.all().values()
    #
    # return render(request, 'weatherstation/charts.html', {'data': data})

def view_logs(request):
    json_send = serialize_bootstraptable(StationLogs.objects.all())

    return JsonResponse(json_send, safe=False)


# Index View
class StationListView(ListView):
    model = Stations
    template_name = 'weatherstation/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'stations'

    def get_context_data(self, **kwargs):
        context = super(StationListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the log
        # context['data'] = StationLogs.objects.all()
        context['data'] = Stations.objects.get(station_id=1).logs.last()
        return context


class ChartListView(ListView):
    model = Stations
    template_name = 'weatherstation/charts.html'
    context_object_name = 'stations'


class StationCreateView(CreateView):
    model = Stations
    fields = ['station_name', 'station_temperature', 'station_humidity', 'station_ambient_light', 'station_pressure',
              'station_altitude', 'station_point', 'station_date_retrieved']

#
# def about(request):
#     def event_stream():
#         while True:
#             time.sleep(3)
#             yield 'data: The server time is: %s\n\n' % datetime.datetime.now()
#     return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

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
    station_name = str(request.POST["station_name"])
    station_temperature = float(request.POST["station_temperature"])
    station_humidity = float(request.POST["station_humidity"])
    station_ambient_light = int(request.POST["station_ambient_light"])
    station_pressure = float(request.POST["station_pressure"])
    station_altitude = float(request.POST["station_altitude"])
    station_point = Point(13.72, 100.77)
    station_pm25 = random.randrange(100)
    station_date_retrieved = timezone.now()

    station = Stations(station_name=station_name,station_temperature=station_temperature,station_humidity=station_humidity,
                      station_ambient_light=station_ambient_light,station_pressure=station_pressure,station_altitude=station_altitude,
                      station_point=station_point,station_pm25=station_pm25,station_date_retrieved=station_date_retrieved)
    station.save()

    context = {
        'title': 'Add Station',
    }

    return render(request, 'weatherstation/add_station_form_submission.html', context)
