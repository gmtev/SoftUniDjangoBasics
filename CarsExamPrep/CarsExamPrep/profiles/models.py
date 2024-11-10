from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from CarsExamPrep.profiles.validators import NameValidator


class Profile(models.Model):
    MIN_LEN_USERNAME = 3
    MAX_LEN_USERNAME = 15
    MAX_LEN_NAME = 25
    MAX_LEN_PASSWORD = 20
    MIN_VALUE_AGE = 21

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=[
            NameValidator(), MinLengthValidator(MIN_LEN_USERNAME,
                                                message=f"Username must be at least {MIN_LEN_USERNAME} chars long!")
        ],
    )
    email = models.EmailField(
        unique=True
    )

    age = models.IntegerField(
        validators=[MinValueValidator(MIN_VALUE_AGE)],
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None