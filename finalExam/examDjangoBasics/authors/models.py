from django.core.validators import MinLengthValidator
from django.db import models
from examDjangoBasics.authors.validators import NameLetterValidator, PassLengthValidator


class Author(models.Model):
    MAX_LEN_FIRST_NAME = 40
    MIN_LEN_FIRST_NAME = 4
    MAX_LEN_LAST_NAME = 50
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_PASSWORD = 6
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=[MinLengthValidator(MIN_LEN_FIRST_NAME), NameLetterValidator()]
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=[MinLengthValidator(MIN_LEN_LAST_NAME), NameLetterValidator()]
    )
    passcode = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=[PassLengthValidator()],
    )
    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True, null=True
    )
    image_url = models.URLField(
        blank=True, null=True
    )
