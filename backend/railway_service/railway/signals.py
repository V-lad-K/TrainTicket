from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CarriageModel, SpotModel, TrainModel


def create_spot(carriage_id):
    spot_count = 54
    side_spot_start_number = int(spot_count - spot_count / 3)
    carriage = CarriageModel.objects.get(id=carriage_id)
    for spot_number in range(1, spot_count+1):
        if spot_number <= side_spot_start_number:
            spot_type = "T" if spot_number % 2 == 0 else "B"
        else:
            spot_type = "S"

        SpotModel.objects.create(type=spot_type, number=spot_number, carriage=carriage)


def create_carriage(train_id):
    carriage_count = 10
    train = TrainModel.objects.get(id=train_id)

    first_class_start_index = 6
    lux_class_start_index = 9
    for carriage_number in range(1, carriage_count+1):
        if carriage_number <= first_class_start_index:
            carriage_type = "S"
        elif first_class_start_index < carriage_number < lux_class_start_index:
            carriage_type = "F"
        else:
            carriage_type = "L"

        CarriageModel.objects.create(
            type=carriage_type,
            number=carriage_number,
            train=train
        )


@receiver(post_save, sender=CarriageModel)
def post_save_carriage_model(sender, instance, created, **kwargs):
    if created:
        create_spot(instance.id)


@receiver(post_save, sender=TrainModel)
def post_save_train_model(sender, instance, created, **kwargs):
    if created:
        create_carriage(instance.id)