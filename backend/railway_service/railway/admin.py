from django.contrib import admin

from .models import (
    TrainModel,
    CarriageModel,
    SpotModel,
    StationModel,
    RoadmapTrainModel,
    RoadmapModel
)


admin.site.register(TrainModel)
admin.site.register(CarriageModel)
admin.site.register(SpotModel)
admin.site.register(StationModel)
admin.site.register(RoadmapTrainModel)
admin.site.register(RoadmapModel)
