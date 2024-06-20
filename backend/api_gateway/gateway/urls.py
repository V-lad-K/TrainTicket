from django.urls import path

from .views import (
    UserRegistrationAPIView,
    UserPasswordResetAPIView,
    UserPasswordResetConfirmationAPIView,
    UserAuthenticationAPIView,
    UserAccountActivationAPIView
)


urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view(), name="user_registration"),
    path('authentication/', UserAuthenticationAPIView.as_view(), name="user_authentication"),
    path('reset_password/', UserPasswordResetAPIView.as_view(), name="user_password_reset"),
    path('reset_password_confirm/', UserPasswordResetConfirmationAPIView.as_view(), name="reset_password_confirm"),
    path("account_activation/", UserAccountActivationAPIView.as_view(), name="account_activation")
]
