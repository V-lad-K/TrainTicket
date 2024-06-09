from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path("", include("gateway.swagger_urls")),
    path('admin/', admin.site.urls),
    path('api/users/', include("gateway.urls"))
]
