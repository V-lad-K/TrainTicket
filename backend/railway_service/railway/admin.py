from django.contrib import admin

from .models import (
    TrainModel,
    CarriageModel,
    SpotModel,
    StationModel,
    RoadmapDetailModel,
    RoadmapModel
)


admin.site.register(TrainModel)
admin.site.register(CarriageModel)
admin.site.register(SpotModel)
admin.site.register(StationModel)
admin.site.register(RoadmapDetailModel)
admin.site.register(RoadmapModel)
