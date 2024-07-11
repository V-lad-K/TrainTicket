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

    def __str__(self):
        return f"{self.departure_station}-{self.destination_station}"


class RoadmapTrainModel(models.Model):
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    roadmap = models.ManyToManyField(RoadmapModel)
    train = models.ManyToManyField(TrainModel)
    stop_number = models.IntegerField()

    # def clean(self):
    #     self.clean_stop_number(self.stop_number)
    def clean(self):
        train_list = list(self.train.all())
        roadmap_list = list(self.roadmap.all())
        roadmap_train = RoadmapTrainModel.objects.filter(train=train_list[0])

        # print("self.train", train_list)
        # print("self.roadmap_list", roadmap_list)
        # print("roadmap_train", roadmap_train)
        # for tr in roadmap_train:
        #     print(tr.__dict__)
        #     trains = tr.train.all()
        #     for train in trains:
        #         print("train", train.type)

        for train in train_list:
            roadmap_trains = RoadmapTrainModel.objects.filter(train=train)
            for roadmap_train in roadmap_trains:
                roadmaps = list(roadmap_train.roadmap.all())
                if len(roadmaps) > 1:
                    for roadmap in roadmaps[-2:]:
                        print("destination_station", roadmap.destination_station)
                        print("roadmaps is", roadmap)
        self.clean_stop_number(self.stop_number)

    def clean_stop_number(self, value):
        if value == 1:
            raise ValidationError("haha")

    def clean_roadmap(self, previous_roadmap):
        current_roadmaps = self.roadmap.all()
        for roadmap in current_roadmaps:
            if previous_roadmap.destination_station != roadmap.departure_station:
                raise ValidationError("Error in station sequence")

    def __str__(self):
        return f"{self.departure_date}-{self.arrival_date}"
