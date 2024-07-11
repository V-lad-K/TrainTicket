from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import RoadmapTrainModel, StationModel, RoadmapModel, TrainModel


class RoadmapTrainModelTestCase(TestCase):
    def setUp(self):
        self.station1 = StationModel.objects.create(name="Station A")
        self.station2 = StationModel.objects.create(name="Station B")
        self.station3 = StationModel.objects.create(name="Station C")
        self.station4 = StationModel.objects.create(name="Station D")

        self.roadmap1 = RoadmapModel.objects.create(
            departure_station=self.station1,
            destination_station=self.station2
        )
        self.roadmap2 = RoadmapModel.objects.create(
            departure_station=self.station2,
            destination_station=self.station3
        )
        self.roadmap3 = RoadmapModel.objects.create(
            departure_station=self.station3,
            destination_station=self.station4
        )

        self.roadmap_invalid = RoadmapModel.objects.create(
            departure_station=self.station1,
            destination_station=self.station4
        )

        self.train1 = TrainModel.objects.create(type="O", number=101)
        self.train2 = TrainModel.objects.create(type="H", number=108)

    # def test_invalid_stop_number(self):
    #     roadmap_train = RoadmapTrainModel(
    #         departure_date="2024-07-10 08:00:00",
    #         arrival_date="2024-07-10 10:00:00",
    #         stop_number=1)
    #     with self.assertRaises(ValidationError):
    #         roadmap_train.full_clean()

    def test_invalid_roadmap(self):
        roadmap_train1 = RoadmapTrainModel(
            departure_date="2024-07-10 08:00:00",
            arrival_date="2024-07-10 10:00:00",
            stop_number=2
        )
        roadmap_train1.save()
        roadmap_train1.roadmap.set([self.roadmap1])
        roadmap_train1.train.set([self.train1])
        roadmap_train1.full_clean()
        roadmap_train1.save()

        roadmap_train2 = RoadmapTrainModel(
            departure_date="2024-08-10 08:00:00",
            arrival_date="2024-08-10 10:00:00",
            stop_number=2
        )
        roadmap_train2.save()
        roadmap_train2.roadmap.set([self.roadmap3])
        roadmap_train2.train.set([self.train1])
        roadmap_train2.full_clean()
        roadmap_train2.save()

        # roadmap_train2 = RoadmapTrainModel(
        #     departure_date="2024-08-10 08:00:00",
        #     arrival_date="2024-08-10 10:00:00",
        #     stop_number=3
        # )
        # roadmap_train2.save()
        # roadmap_train2.roadmap.set([self.roadmap_invalid])
        # roadmap_train2.train.set([self.train1])

        # roadmap_train3 = RoadmapTrainModel(
        #     departure_date="2024-12-10 08:00:00",
        #     arrival_date="2024-14-10 10:00:00",
        #     stop_number=4
        # )
        # roadmap_train3.save()
        # roadmap_train3.roadmap.set([self.roadmap_invalid])
        # roadmap_train3.train.set([self.train2])
        # roadmap_train3.full_clean()
        # roadmap_train3.save()
        # with self.assertRaises(ValidationError):
        #     roadmap_train2.full_clean()
