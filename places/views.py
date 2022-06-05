from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import get_object_or_404

from .models import Place


def fetch_place_title(
        request: HttpRequest,
        place_id: int,
) -> HttpResponse:

    place = get_object_or_404(Place, pk=place_id)
    return HttpResponse(place.title)
