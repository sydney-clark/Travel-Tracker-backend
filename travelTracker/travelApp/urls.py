from django.urls import path
from . import views

urlpatterns = [
    path('api/travelApp', views.TravelList.as_view(), name='travel_list'), 
    path('api/travelApp/<int:pk>', views.TravelDetail.as_view(), name='travel_detail'), 
]