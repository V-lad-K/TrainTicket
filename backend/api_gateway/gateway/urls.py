from django.urls import path

from .views import UserRegistration
from .views import UserPasswordReset
from .views import UserPasswordResetConfirmation


urlpatterns = [
    path('registration/', UserRegistration.as_view(), name="user_registration"),
    path('reset_password/', UserPasswordReset.as_view(), name="user_password_reset"),
    path('reset_password_confirm/', UserPasswordResetConfirmation.as_view(), name="reset_password_confirm"),
]
