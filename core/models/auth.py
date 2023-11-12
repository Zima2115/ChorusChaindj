from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField("email address", unique=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": "This username is taken.",
        },
        null=True,
        blank=True
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        if self.username:
            return self.username
        return self.get_username()


class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)




    def __str__(self):
        return self.account.__str__()

