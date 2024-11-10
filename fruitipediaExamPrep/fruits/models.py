from django.db import models
from django.core.validators import MinLengthValidator
from fruits.validators import FruitNameValidator


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(2), FruitNameValidator()],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one."
        }
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True, null=True
    )
    owner = models.ForeignKey(
        to='profiles.Profile', on_delete=models.CASCADE, related_name='fruits'
    )
