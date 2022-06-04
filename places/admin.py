from django.contrib import admin

from .models import (
    Image,
    Place,
)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = 'title', 'description_short',


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = 'position', 'title',
