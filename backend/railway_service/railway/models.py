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
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
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

    def __str__(self):
        return f"{self.departure_date}-{self.arrival_date}"


class RoadmapTrainModel(models.Model):
    roadmap = models.ManyToManyField(RoadmapModel)
    train = models.ManyToManyField(TrainModel)
    stop_number = models.IntegerField()

    def clean_stop_number(self, value):
        print("JJJJJJJJJJJJJJJJJJJJJ")
        if value == 1:
            raise "haha"
    # def clean(self):
    #
    #     for train in TrainModel.objects.all():
    #         roadmaps = RoadmapTrainModel.objects.filter(train=train)
    #         print("roadmaps", roadmaps)
    #         previous_destination_station = None
    #         for roadmap_train in roadmaps:
    #             for roadmap in roadmap_train.roadmap.all():
    #                 if previous_destination_station and previous_destination_station != roadmap.departure_station:
    #                     print(previous_destination_station, roadmap.departure_station)
    #                     raise ValidationError(
    #                         f"Маршрут для потяга {train} не може починатися з {roadmap.departure_station}, бо попередній маршрут закінчується на {previous_destination_station}.")
    #                 previous_destination_station = roadmap.destination_station

