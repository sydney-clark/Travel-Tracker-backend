from django.urls import path
from . import views

urlpatterns = [
    path('api/travelList', views.TravelList.as_view(), name='travel_list'), 
    path('api/travelList/<int:pk>', views.TravelDetail.as_view(), name='travel_detail'), 
    path('api/markerList', views.MarkerList.as_view(), name='marker_list'), 
    path('api/markerList/<int:pk>', views.MarkerDetail.as_view(), name='marker_detail'),
]