from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from CarsExamPrep.cars.choices import TypeChoices


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 15
    MIN_LEN_MODEL = 1
    MIN_YEAR = 1999
    MAX_YEAR = 2030
    MIN_PRICE = 1.0
    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=TypeChoices.choices,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=[MinLengthValidator(MIN_LEN_MODEL)]
    )
    year = models.IntegerField(
        validators=[MinValueValidator(MIN_YEAR, message=ERROR_MESSAGE_YEAR),
                    MaxValueValidator(MAX_YEAR, message=ERROR_MESSAGE_YEAR)]
    )
    image_url = models.URLField(
        unique=True,
    )

    price = models.FloatField(
        validators=[MinValueValidator(MIN_PRICE)],
    )
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars',
    )
