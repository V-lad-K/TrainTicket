import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField(
        blank=False,
        unique=True
    )

    def clean(self):
        super().clean()

        self.clean_username()
        self.clean_email()
        self.clean_password()

    def clean_username(self):
        if " " in self.username:
            raise ValidationError("Username must not contain spaces")
        if 5 <= len(self.username) <= 150:
            raise ValidationError("Username must be in range 5 - 150")
        if not re.match("^[A-Za-z0-9_]*$", self.username):
            raise ValidationError("Username should contain only latin letters, numbers, underscores")

    def clean_email(self):
        if not 10 <= len(self.username) <= 150:
            raise ValidationError("Username must be in range 5 - 150")
        if len(self.username.split("@")[0]) < 5:
            raise ValidationError("Local part of email must be more 5 characters")
        if len(self.username.split("@")[1]) < 5:
            raise ValidationError("Domain part of email must be more 5 characters")
        if not re.match("^[A-Za-z0-9]*$", self.username[0]):
            raise ValidationError("First letter of email must be letter")
        if not re.match("^[A-Za-z0-9._-]*$", self.username):
            raise ValidationError("Username should contain only latin letters, numbers, underscores")
        if not re.match("^[A-Za-z0-9]+([._-][A-Za-z0-9]+)*$", "hghgh__fgh5654_64-f"):
            raise ValidationError("An underscore, period, or dash must be followed by one or more letter or number")

    def clean_password(self):
        if not 8 <= len(self.username) <= 150:
            raise ValidationError("Username must be in range 8 - 150")
        if not any([char.isupper() for char in self.username]):
            raise ValidationError("Password must have at least 1 upper character")
        if not any([char.isdigit() for char in self.username]):
            raise ValidationError("Password must have at least 1 digit")
        if not re.match("^[A-Za-z0-9]+([._-][A-Za-z0-9]+)*$", self.username):
            raise ValidationError("the password must not contain Cyrillic characters")
