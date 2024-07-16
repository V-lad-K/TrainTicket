from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CarriageModel
from .tasks import create_second_class_spots


@receiver(post_save, sender=CarriageModel)
def post_save_carriage_model(sender, instance, created, **kwargs):
    if created:
        create_second_class_spots.delay(instance.carriage)
