from django.db import models


class Place(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        db_index=False,
    )
    description_short = models.CharField(
        max_length=100,
        blank=False,
    )
    description_long = models.TextField(
        blank=False,
    )
    coordinates = models.JSONField(
        blank=False,
        unique=True,
    )
