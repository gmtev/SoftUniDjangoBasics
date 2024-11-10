from django.core.validators import MinLengthValidator
from profiles.validators import NameValidator
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(2), NameValidator()],
    )
    last_name = models.CharField(
        max_length=35,
        validators=[MinLengthValidator(1), NameValidator()],
    )
    email = models.EmailField(
        max_length=40,
        unique=True
    )
    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8),],
        help_text="*Password length requirements: 8 to 20 characters"
    )
    image_url = models.URLField(
        blank=True, null=True
    )
    age = models.IntegerField(
        default=18
    )
