from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_station/', views.add_station, name='add_station'),
    path('add_station_form_submission/', views.add_station_form_submission, name='add_station_form_submission'),
]