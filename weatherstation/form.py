from django.contrib.gis import forms
from mapwidgets.widgets import GooglePointFieldWidget


class CityAdminForm(forms.ModelForm):
    class Meta:
        model = "Thailand"
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GooglePointFieldWidget,
        }