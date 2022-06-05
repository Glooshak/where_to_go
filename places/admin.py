from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Image,
    Place,
)


class ImageInLine(admin.TabularInline):
    model = Image
    readonly_fields = 'get_preview',

    def get_preview(self: 'ImageInLine', image: Image) -> str:
        picture = image.picture
        url, height, width = picture.url, picture.height, picture.width
        if height > 200:
            old_aspect_ratio = height / width
            height = 200
            width = height / old_aspect_ratio
            new_aspect_ratio = height / width
            assert new_aspect_ratio == old_aspect_ratio, 'Aspect ration was not preserved!'

        return format_html(
            f'<img src="{url}" width="{width}" height={height} />'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = 'title', 'description_short',
    inlines = ImageInLine,


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = 'position', 'title',
