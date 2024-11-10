from django.db import models
from django.core.validators import MinLengthValidator
from musicAppExamPrep.profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(max_length=15, validators= [MinLengthValidator(2),
                                                            UsernameValidator()])
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)