from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    MAX_LEN_TITLE = 50
    MIN_LEN_TITLE = 5
    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        validators=[MinLengthValidator(MIN_LEN_TITLE)],
    )
    image_url = models.URLField()

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True
    )
    author = models.ForeignKey(
        'authors.Author',
        on_delete=models.CASCADE,
        related_name="posts"
    )
