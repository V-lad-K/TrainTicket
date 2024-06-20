from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    # EMAIL_FIELD = 'email'

    email = models.EmailField(
        blank=False,
        unique=True
    )
