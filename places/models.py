from django.db import models


class Place(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        db_index=False,
    )

    description_short = models.CharField(
        max_length=300,
        blank=False,
    )

    description_long = models.TextField(
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


class Image(models.Model):

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE
    )

    picture_name = models.CharField(
        max_length=50,
        blank=False,
        db_index=False,
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
        return self.picture_name

    class Meta:
        ordering = ['position']
