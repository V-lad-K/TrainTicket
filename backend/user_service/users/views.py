import time
from django.http import HttpResponse
from .tasks import


def index(request):
    send.delay(10)
    # timesleep(10)
    return HttpResponse("mail")
