# -*- coding: utf-7 -*-
from django.db import models

# Create your models here.
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    Region = models.CharField(max_length=32)
    Regional_Drought_Stage = models.CharField(max_length=32)
    Reservoir_Name = models.CharField(max_length=32)
    Reservoir_Storage = models.DecimalField(max_digits=10, decimal_places=4)
    Reservoir_Level = models.DecimalField(max_digits=7, decimal_places=4)
    Date = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"

    def __str__(self):
        return "%s %s %s" % (self.county, self.sid, self.name)

class Rainfall(models.Model):
    rpk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    sid = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=25)
    r_10m = models.FloatField(blank=True, null=True)
    r_1h = models.FloatField(blank=True, null=True)
    r_3h = models.FloatField(blank=True, null=True)
    r_6h = models.FloatField(blank=True, null=True)
    r_12h = models.FloatField(blank=True, null=True)
    r_24h = models.FloatField(blank=True, null=True)
    r_td = models.FloatField(blank=True, null=True)
    r_yd = models.FloatField(blank=True, null=True)
    r_2d = models.FloatField(blank=True, null=True)
    station = models.ForeignKey(Station)

    class Meta:
        verbose_name = "Rainfall"
        verbose_name_plural = "Rainfalls"

    def __str__(self):
        return "%s %s %s" % (self.sid, self.name, self.timestamp)

