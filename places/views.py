from django.http import (
    HttpRequest,
    JsonResponse,
)
from django.shortcuts import get_object_or_404

from .models import Place


def fetch_place(
        request: HttpRequest,
        place_id: int,
) -> JsonResponse:

    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(
        {
            'title': place.title,
            'imgs': [
                image.picture.url for image in place.image_set.all()
            ],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lat': place.lat,
                'lng': place.lng,
            },
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4},
    )
