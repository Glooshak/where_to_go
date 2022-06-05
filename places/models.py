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

    place_id = models.CharField(
        max_length=15,
        blank=False,
    )

    @property
    def lng(self) -> float:
        return float(self.coordinates['lng'])

    @property
    def lat(self) -> float:
        return float(self.coordinates['lat'])

    def __str__(self) -> str:
        return self.title


class Image(models.Model):

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=50,
        blank=False,
        db_index=False,
    )

    position = models.IntegerField(
        blank=False,
    )

    picture = models.ImageField(
        blank=False,
    )

    def __str__(self) -> str:
        return self.title
