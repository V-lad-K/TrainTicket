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

    def __str__(self):
        return f"train_{self.type}_{self.number}"


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


class SpotDetailModel(models.Model):
    departure_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name="departure_spot_set"
    )
    destination_station = models.ForeignKey(
        StationModel,
        on_delete=models.CASCADE,
        related_name='destination_spot_set'
    )
    spot = models.ForeignKey(
        SpotModel,
        on_delete=models.CASCADE,
        related_name="spot_detail"
    )
    customer_id = models.IntegerField(
        null=True
    )

    def clean(self):
        self.validate_spot_already_sold()

    def validate_spot_already_sold(self):
        spot = SpotModel.objects.get(id=self.spot.id)
        train = spot.carriage.train
        roadmap = RoadmapModel.objects.get(train=train)

        spots = SpotDetailModel.objects.filter(spot=self.spot)
        for spot in spots:
            overlapping_tickets = RoadmapDetailModel.objects.filter(
                roadmap=roadmap,
                departure_station__lt=spot.destination_station,
                destination_station__gt=spot.departure_station
            ).exclude(id=self.id)

            roadmap_list = [overlapping_ticket.departure_station for overlapping_ticket in overlapping_tickets]
            if self.departure_station in roadmap_list:
                raise ValidationError("The spot is already booked for part of this route.")

    def __str__(self):
        return f"detail_spot_{self.spot}"


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
        self.quantity_roadmap_detail = len(list(RoadmapDetailModel.objects.filter(roadmap=self.roadmap)))
        roadmap_detail_objects = RoadmapDetailModel.objects.filter(roadmap=self.roadmap)
        self.previous_station_roadmap = RoadmapDetailModel.objects.filter(
            roadmap=self.roadmap,
            destination_station=self.departure_station
        ).first() if roadmap_detail_objects.exists() else None

        self.validate_roadmap_start_station()
        self.validate_roadmap()
        self.validate_equal_departure_station_destination_station()
        self.validate_end_road()
        self.validate_equal_date()
        self.validate_departure_date()

    def validate_roadmap_start_station(self):
        if not self.quantity_roadmap_detail and self.roadmap.departure_station != self.departure_station:
            raise ValidationError("first roadmap detail has been departure station from roadmap")

    def validate_roadmap_destination_position(self):
        if self.departure_station == self.destination_station:
            raise ValidationError("departure station and destination station can't be identical")

    def validate_roadmap(self):
        if not self.previous_station_roadmap and self.quantity_roadmap_detail:
            raise ValidationError("next departure station must be previous destination station")

    def validate_equal_departure_station_destination_station(self):
        if self.departure_station == self.destination_station:
            raise ValidationError("departure_station must be not equal destination_station")

    def validate_equal_date(self):
        if self.departure_date == self.arrival_date:
            raise ValidationError("departure_date must be not equal departure_date in roadmap")

    def validate_departure_date(self):
        if self.quantity_roadmap_detail and self.departure_date < self.previous_station_roadmap.arrival_date:
            raise ValidationError("departure date must be later then arrival date from previous roadmap")

    def validate_end_road(self):
        if (self.previous_station_roadmap and
                self.previous_station_roadmap.destination_station == self.roadmap.destination_station):
            raise ValidationError("Roadmap is over")

    def __str__(self):
        return f"{self.departure_date}-{self.arrival_date}"
