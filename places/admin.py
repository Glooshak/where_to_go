from django.contrib import admin

from .models import (
    Image,
    Place,
)


class ImageInLine(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = 'title', 'description_short',
    inlines = ImageInLine,


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = 'position', 'title',
