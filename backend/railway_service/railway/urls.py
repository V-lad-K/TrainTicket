from django.urls import path, include
from .views import RailwayListAPIView

urlpatterns = [
    path("get_trains/<str:departure_station>/<str:destination_station>/", RailwayListAPIView.as_view()),
]
