import requests
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserRegistrationSerializer,
    UserAuthorizationSerializer,
    UserResetPasswordSerializer,
    UserResetPasswordConfirmationSerializer,
    UserAccountActivationSerializer
)

from dotenv import load_dotenv
from drf_yasg.utils import swagger_auto_schema

load_dotenv()


class BaseUserMicroserviceAPIView(APIView):
    BASE_URL = os.getenv("BASE_USER_SERVICE_URL")

    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        self.url = url

    def post(self, request):
        response = requests.post(self.url, json=request.data)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response(response, status=response.status_code)
        return Response(response.json(), status=response.status_code)


class UserRegistrationAPIView(BaseUserMicroserviceAPIView):
    REGISTRATION_URL = "auth/users/"

    def __init__(self):
        url = self.BASE_URL + self.REGISTRATION_URL
        super().__init__(url)

    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        return super().post(request)


class UserAuthenticationAPIView(BaseUserMicroserviceAPIView):
    AUTHENTICATION_URL = "auth/jwt/create/"

    def __init__(self):
        url = self.BASE_URL + self.AUTHENTICATION_URL
        super().__init__(url)

    @swagger_auto_schema(request_body=UserAuthorizationSerializer)
    def post(self, request):
        return super().post(request)


class UserPasswordResetAPIView(BaseUserMicroserviceAPIView):
    RESET_PASSWORD_URL = "auth/users/reset_password/"

    def __init__(self):
        url = self.BASE_URL + self.RESET_PASSWORD_URL
        super().__init__(url)
    
    @swagger_auto_schema(request_body=UserResetPasswordSerializer)
    def post(self, request):
        return super().post(request)


class UserPasswordResetConfirmationAPIView(BaseUserMicroserviceAPIView):
    RESET_PASSWORD_CONFIRMATION_URL = "auth/users/reset_password_confirm/"

    def __init__(self):
        url = self.BASE_URL + self.RESET_PASSWORD_CONFIRMATION_URL
        super().__init__(url)

    @swagger_auto_schema(request_body=UserResetPasswordConfirmationSerializer)
    def post(self, request):
        return super().post(request)


class UserAccountActivationAPIView(BaseUserMicroserviceAPIView):
    ACTIVATION_URL = "auth/users/activation/"

    def __init__(self, **kwargs):
        url = self.BASE_URL + self.ACTIVATION_URL
        super().__init__(url, **kwargs)

    @swagger_auto_schema(request_body=UserAccountActivationSerializer)
    def post(self, request):
        return super().post(request)
