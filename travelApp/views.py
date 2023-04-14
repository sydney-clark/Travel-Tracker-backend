# from django.shortcuts import render
from rest_framework import generics
from .serializers import TravelSerializer, MarkerSerializer
from .models import Travel, Marker

# Create your views here.
class TravelList(generics.ListCreateAPIView): #read(index) and create route
    queryset = Travel.objects.all().order_by('id')     # what are we retrieving? -- retrieve all objects from the DB, order by id ascending
    serializer_class = TravelSerializer    # tell django what serializer to use

class TravelDetail(generics.RetrieveUpdateDestroyAPIView): #show, update and delete route
    queryset = Travel.objects.all().order_by('id') # this is not a typo...these two are exactly alike but DRF requires it 
    serializer_class = TravelSerializer

class MarkerList(generics.ListCreateAPIView): #read(index) and create route
    queryset = Marker.objects.all().order_by('id')     # what are we retrieving? -- retrieve all objects from the DB, order by id ascending
    serializer_class = MarkerSerializer    # tell django what serializer to use

class MarkerDetail(generics.RetrieveUpdateDestroyAPIView): #show, update and delete route
    queryset = Marker.objects.all().order_by('id') # this is not a typo...these two are exactly alike but DRF requires it 
    serializer_class = MarkerSerializer
