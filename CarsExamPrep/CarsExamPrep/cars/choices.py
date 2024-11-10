from django.db import models


class TypeChoices(models.TextChoices):
    RALLY = 'Rally', 'Rally'
    OPENWHEEL = 'Open-Wheel', 'Open-Wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'
