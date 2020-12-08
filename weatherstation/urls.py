# from django.urls import path
# from .views import StationListView, ChartListView
#
# urlpatterns = [
#     path('', StationListView.as_view(), name='index'),
#     path('charts/', ChartListView.as_view(), name='charts'),
# ]

from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts/', views.charts, name='charts')
]

urlpatterns += staticfiles_urlpatterns()
