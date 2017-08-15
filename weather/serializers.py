from rest_framework import serializers
from weather.models import Rainfall, Station

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__' 

class FlowobservatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Flowobservatory
        fields = '__all__' 

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = '__all__'

class ForecastingtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecastingtime
        fields = '__all__'
        
class IrrigationareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irrigationarea
        fields = '__all__'
        
class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
class NextreservoirlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nextreservoirlights
        fields = '__all__'
        
class NextweekpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nextweekp
        fields = '__all__'
        
class PrewaterlevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prewaterlevel
        fields = '__all__'
        
class PrewaterstoragecapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Prewaterstoragecapacity
        fields = '__all__'
        
class Q90Serializer(serializers.ModelSerializer):
    class Meta:
        model = Q90
        fields = '__all__'
        
class Q95Serializer(serializers.ModelSerializer):
    class Meta:
        model = Q95
        fields = '__all__'
        
class RegionalwaterregimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regionalwaterregime
        fields = '__all__'
        
class ReservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = '__all__'
        
class ReservoirstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoirstate
        fields = '__all__'
        
class RulecurveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rulecurve
        fields = '__all__'
        
class SimreservoirflowstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simreservoirflow
        fields = '__all__'
        
class WaterintakestructuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterintakestructures
        fields = '__all__'
        
class WatersupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Watersupply
        fields = '__all__'