from django.contrib import admin
from .models import Station

# from django.contrib.gis.db import models
# from mapwidgets.widgets import GooglePointFieldWidget


admin.site.register(Station)


# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget},
#     }