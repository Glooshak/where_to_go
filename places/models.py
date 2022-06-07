from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        db_index=False,
        unique=True,
    )

    description_short = models.CharField(
        max_length=300,
        blank=False,
    )

    description_long = HTMLField(
        blank=False,
    )

    lng = models.FloatField(
        blank=False,
    )

    lat = models.FloatField(
        blank=False,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = 'id',
        unique_together = 'lng', 'lat',


class Image(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
    )

    position = models.PositiveIntegerField(
        blank=False,
        default=0,
        null=False,
    )

    picture = models.ImageField(
        blank=False,
    )

    def __str__(self) -> str:
        return self.place.title

    class Meta:
        ordering = ['position']
