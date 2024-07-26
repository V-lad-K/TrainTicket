from rest_framework.generics import (
    ListAPIView,
    get_object_or_404
)
from .models import (
    RoadmapModel,
    RoadmapDetailModel,
    StationModel
)
from .serializers import RailwaySerializer


class RailwayListAPIView(ListAPIView):
    """
        API view to retrieve a list of trains and their roadmaps for specific order.
    """

    serializer_class = RailwaySerializer

    def get_queryset(self):
        departure_station_name = self.kwargs["departure_station"]
        destination_station_name = self.kwargs["destination_station"]

        departure_station = get_object_or_404(StationModel, name=departure_station_name)
        destination_station = get_object_or_404(StationModel, name=destination_station_name)

        roadmap_queryset = RoadmapModel.objects.all()
        result_queryset = []

        for roadmap in roadmap_queryset:
            roadmap_details = RoadmapDetailModel.objects.filter(roadmap=roadmap)
            full_roadmap = (
                    [roadmap_detail.departure_station for roadmap_detail in roadmap_details] +
                    [roadmap_details.last().destination_station]
            )

            if (departure_station in full_roadmap and
                    destination_station in full_roadmap and
                    full_roadmap.index(destination_station) > full_roadmap.index(departure_station)):
                result_queryset.append(roadmap)

        return result_queryset
