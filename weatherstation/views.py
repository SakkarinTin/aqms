from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from django.http import JsonResponse

from .models import Stations, StationLogs
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime

import random, requests as req, json
from .utils import serialize_bootstraptable


def index(request):
    context = {
        'stationlogs': StationLogs.objects.all()
    }

    return render(request, 'weatherstation/index.html', context)


def logs(request):
    context = {
        'stationlogs': StationLogs.objects.all()
    }

    return render(request, 'weatherstation/logs.html', context)

    # data = StationLogs.objects.all().values()
    #
    # return render(request, 'weatherstation/charts.html', {'data': data})


def data(request):
    context = {
        'stationlogs': StationLogs.objects.all()
    }

    return render(request, 'weatherstation/data.html', context)


def AjaxHandlerView(request):
    data = []
    last_data_station1 = Stations.objects.get(station_id=1).logs.last()
    last_data_station2 = Stations.objects.get(station_id=2).logs.last()
    # Set time to naturaltime
    station1_natural_time = str(naturaltime(last_data_station1.station_recorded_time))
    station2_natural_time = str(naturaltime(last_data_station2.station_recorded_time))

    data.extend((
            # Append Station 1 all data
            {'station1_temperature':    str(last_data_station1.station_temperature)[:-1] },
            {'station1_humidity':       str(last_data_station1.station_humidity)[:-1] },
            {'station1_pm25':           last_data_station1.station_pm25 },
            {'station1_pm10':           last_data_station1.station_pm10 },
            {'station1_latitude':       last_data_station1.station_latitude },
            {'station1_longitude':      last_data_station1.station_longitude },
            {'station1_recorded_time':  station1_natural_time },
            # Append Station 2 all data
            {'station2_temperature':    str(last_data_station2.station_temperature)[:-1] },
            {'station2_humidity':       str(last_data_station2.station_humidity)[:-1] },
            {'station2_pm25':           last_data_station2.station_pm25 },
            {'station2_pm10':           last_data_station2.station_pm10 },
            {'station2_latitude':       last_data_station2.station_latitude },
            {'station2_longitude':      last_data_station2.station_longitude },
            {'station2_recorded_time':  station2_natural_time },
        ))

    # return render(request, 'weatherstation/index.html', json.dumps(data))
    return JsonResponse(data, safe=False)


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
