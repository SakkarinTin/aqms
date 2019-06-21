from django.urls import path
from .views import StationListView, StationCreateView, ChartListView
from . import views

urlpatterns = [
    path('', StationListView.as_view(), name='index'),
    path('charts/', ChartListView.as_view(), name='charts'),
    path('station/new/', StationCreateView.as_view(), name='station-create'),
    path('about/', views.about, name='about'),
    path('add_station/', views.add_station, name='add_station'),
    path('add_station_form_submission/', views.add_station_form_submission, name='add_station_form_submission'),
]