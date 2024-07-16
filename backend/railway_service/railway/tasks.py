from celery import shared_task
from .models import SpotModel


@shared_task
def create_second_class_spots(carriage):
    count = 54
    side_spot_start_number = int(count - count / 3)

    for spot_number in range(count):
        if spot_number < side_spot_start_number:
            spot_type = "T" if spot_number % 2 == 0 else "B"
        else:
            spot_type = "S"

        SpotModel.objects.create(type=spot_type, number=spot_number, carriage=carriage)
