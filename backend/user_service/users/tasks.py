from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(subject, message, from_email, to_email):
    send_mail(subject, message, from_email, [to_email])
    # send_mail(subject, message, from_email, to_email)


@shared_task
def add(x, y):
    return x + y


@shared_task
def timesleep(time):
    sleep(time)
    return None


@shared_task
def send(time):
    send_mail("subject", "message", "krugonovskiy@gmail.com",
              ["vladyslav.kryzhanivskyi.mpmpm.2023@lpnu.ua"])
    return None
