from django.urls import path
from .views import StationListView, ChartListView

urlpatterns = [
    path('', StationListView.as_view(), name='index'),
    path('charts/', ChartListView.as_view(), name='charts'),
]




