# Generated by Django 2.2.1 on 2019-12-15 15:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('battery_level', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Station',
                'verbose_name_plural': 'Stations',
                'ordering': ['station_id'],
            },
        ),
        migrations.CreateModel(
            name='StationLogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_temperature', models.DecimalField(decimal_places=2, max_digits=10)),
                ('station_humidity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('station_pm25', models.IntegerField()),
                ('station_pm10', models.IntegerField()),
                ('station_pm1', models.IntegerField()),
                ('station_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('station_latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('station_longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('station_recorded_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='weatherstation.Stations')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'ordering': ['log_id', '-station_recorded_time'],
            },
        ),
    ]
