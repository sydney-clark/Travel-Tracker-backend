from rest_framework import serializers 
from .models import Travel, Marker

class TravelSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Travel # tell django which model to use
        fields = ('id', 'location', 'type', 'date', 'address', 'contact') # tell django which fields to include

class MarkerSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Marker # tell django which model to use
        fields = ('id', 'address', 'latitude', 'longitude') # tell django which fields to include
