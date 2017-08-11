from rest_framework import serializers
from weather.models import Rainfall, Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__' 

class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = '__all__' 
