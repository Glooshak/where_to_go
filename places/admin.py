from adminsortable2.admin import (
    SortableAdminMixin,
    SortableInlineAdminMixin,
)
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Image,
    Place,
)


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = 'get_preview',

    MAX_PICTURE_HEIGHT = 200

    def get_preview(self: 'ImageInLine', image: Image) -> str:
        picture = image.picture
        url, height, width = picture.url, picture.height, picture.width
        if height > self.MAX_PICTURE_HEIGHT:
            old_aspect_ratio = height / width
            height = self.MAX_PICTURE_HEIGHT
            width = height / old_aspect_ratio

        return format_html(
            f'<img src="{url}" width="{width}" height={height} />'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = 'title', 'description_short',
    inlines = ImageInLine,


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = 'position', 'place',
