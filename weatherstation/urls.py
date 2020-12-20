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
    path('logs-history/', views.logs, name='logs'),
    path('get/ajax', views.AjaxHandlerView, name = "AjaxHandlerView")
]

# urlpatterns += staticfiles_urlpatterns()
