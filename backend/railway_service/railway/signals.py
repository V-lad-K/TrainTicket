from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CarriageModel, SpotModel


def create_spot(carriage_id):
    count = 54
    side_spot_start_number = int(count - count / 3)
    carriage = CarriageModel.objects.get(id=carriage_id)
    for spot_number in range(1, count+1):
        if spot_number <= side_spot_start_number:
            spot_type = "T" if spot_number % 2 == 0 else "B"
        else:
            spot_type = "S"

        SpotModel.objects.create(type=spot_type, number=spot_number, carriage=carriage)


@receiver(post_save, sender=CarriageModel)
def post_save_carriage_model(sender, instance, created, **kwargs):
    if created:
        create_spot(instance.id)
