# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from weather.models import Rainfall, Station
from weather.serializers import RainfallSerializer, StationSerializer
from rest_framework import generics

class RainfallList(generics.ListAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class RainfallDetail(generics.RetrieveAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class StationList(generics.ListAPIView):
    serializer_class = StationSerializer
    
    def get_queryset(self):
        queryset = Station.objects.all()
        Region = self.request.query_params.get('Region', None)
        Date = self.request.query_params.get('Date', None)
        if Region is not None and Date is not None:
            queryset = queryset.filter(Region=Region).filter(Date=Date)
        elif Region is not None :                                                    
             queryset = queryset.filter(Region=Region)
        elif Date is not None :                                                    
             queryset = queryset.filter(Date=Date)
        return queryset

