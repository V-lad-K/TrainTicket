from rest_framework import serializers
from .models import RoadmapModel


class RailwaySerializer(serializers.ModelSerializer):
    departure_station = serializers.CharField(max_length=255)
    destination_station = serializers.CharField(max_length=255)

    class Meta:
        model = RoadmapModel
        fields = '__all__'
