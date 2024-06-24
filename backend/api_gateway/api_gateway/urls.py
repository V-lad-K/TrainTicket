from django.contrib import admin
from django.urls import path
from django.urls import include

from gateway.swagger import swagger_urlpatterns

urlpatterns = [
    path("", include(swagger_urlpatterns)),
    path('admin/', admin.site.urls),
    path('api/users/', include("gateway.urls"))
]
