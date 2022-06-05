from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.template import loader
from django.urls import reverse

from places.models import Place


def show_main_page(
        request: HttpRequest,
) -> HttpResponse:
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in Place.objects.all():
        place_id = place.place_id
        geo_json['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place_id,
                    "detailsUrl": reverse('places', kwargs={'place_id': place.id})
                }
            }
        )
    return HttpResponse(
        loader.get_template('index.html').render({'geo_json': geo_json}, request)
    )
