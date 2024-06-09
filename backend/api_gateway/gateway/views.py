import requests
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dotenv import load_dotenv

load_dotenv()


class BaseUserMicroservice(APIView):
    BASE_URL = os.getenv("BASE_USER_SERVICE_URL")

    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        self.url = url

    def post(self, request):
        response = requests.post(self.url, json=request.data)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response(response)
        return Response(response.json())


class UserRegistration(BaseUserMicroservice):
    REGISTRATION_URL = "auth/users/"

    def __init__(self):
        url = self.BASE_URL + self.REGISTRATION_URL
        super().__init__(url)


class UserPasswordReset(BaseUserMicroservice):
    RESET_PASSWORD_URL = "auth/users/reset_password/"

    def __init__(self):
        url = self.BASE_URL + self.RESET_PASSWORD_URL
        super().__init__(url)


class UserPasswordResetConfirmation(BaseUserMicroservice):
    RESET_PASSWORD_CONFIRMATION_URL = "auth/users/reset_password_confirm/"

    def __init__(self):
        url = self.BASE_URL + self.RESET_PASSWORD_CONFIRMATION_URL
        super().__init__(url)
