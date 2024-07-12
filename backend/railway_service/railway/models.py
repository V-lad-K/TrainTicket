from django.db import models
from django.core.exceptions import ValidationError


class TrainModel(models.Model):
    class TrainTypeModel(models.TextChoices):
        ORDINARY = "O", "Ordinary"
        HIGH_SPEED = "H", "High speed"

    type = models.CharField(
        max_length=1,
        choices=TrainTypeModel,
        default=TrainTypeModel.HIGH_SPEED
    )
    number = models.IntegerField()


class CarriageModel(models.Model):
    class CarriageTypeModel(models.TextChoices):
        SECOND_CLASS = "S", "Second class"
        FIRST_CLASS = "F", "First class"
        LUX_CLASS = "L", "Lux class"

    type = models.CharField(
        max_length=1,
        choices=CarriageTypeModel,
        default=CarriageTypeModel.SECOND_CLASS
    )
    number = models.IntegerField()
    train = models.ForeignKey(
        TrainModel,
        on_delete=models.CASCADE,
    )
    spot_numbers = models.IntegerField()

    def __str__(self):
        return f"Carriage_{self.number}_{self.train}"


class SpotModel(models.Model):
    class SpotTypeModel(models.TextChoices):
        BOTTOM = "B", "Bottom"
        TOP = "T", "Top"
        SIDE = "S", "Side"

    type = models.CharField(
        max_length=1,
        choices=SpotTypeModel,
        default=SpotTypeModel.BOTTOM
    )
    number = models.IntegerField()
    carriage = models.ForeignKey(
        CarriageModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"spot_{self.id}"


class StationModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoadmapModel(models.Model):
    departure_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name="departure_set"
    )
    destination_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name='destination_set'
    )

    train = models.ForeignKey(
        TrainModel,
        on_delete=models.CASCADE,
        related_name="roadmap_train",
        null=True
    )

    def __str__(self):
        return f"{self.departure_station}-{self.destination_station}"


class RoadmapDetailModel(models.Model):
    departure_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name="departure_station_detail"
    )
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    destination_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name='destination_station_detail'
    )
    roadmap = models.ForeignKey(
        RoadmapModel,
        on_delete=models.CASCADE,
        null=True
    )

    def clean(self):
        # print("station1  is", self.departure_station)
        # print("roadmap is", self.roadmap)
        # print("roadmap first station", self.roadmap.departure_station)
        # print(self.departure_station == self.roadmap.departure_station)
        self.validate_roadmap_start_station()
        self.validate_roadmap()
        # roadmap = RoadmapModel.objects.get(departure_station=self.departure_station)

    def validate_roadmap_start_station(self):
        quantity_roadmap_detail = len(list(RoadmapDetailModel.objects.filter(roadmap=self.roadmap)))
        if not quantity_roadmap_detail and self.roadmap.departure_station != self.departure_station:
            raise ValidationError("first roadmap detail has been departure station from roadmap")

    def validate_roadmap_destination_position(self):
        if self.departure_station == self.destination_station:
            raise ValidationError("departure station and destination station can't be identical")

    def validate_roadmap(self):
        roadmap_detail_objects = RoadmapDetailModel.objects.filter(roadmap=self.roadmap)
        previous_station_roadmap = RoadmapDetailModel.objects.get(
            roadmap=self.roadmap,
            destination_station=self.departure_station
        ) if roadmap_detail_objects.exists() else None

        if previous_station_roadmap and previous_station_roadmap.destination_station != self.departure_station:
            raise ValidationError("next departure station must be previous destination station")


    def clean_roadmap(self, previous_roadmap):
        current_roadmaps = self.roadmap.all()
        for roadmap in current_roadmaps:
            if previous_roadmap.destination_station != roadmap.departure_station:
                raise ValidationError("Error in station sequence")

    def __str__(self):
        return f"{self.departure_date}-{self.arrival_date}"
