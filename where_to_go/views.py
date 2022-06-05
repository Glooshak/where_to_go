from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.template import loader

from places.models import Place


def show_main_page(
        request: HttpRequest,
) -> HttpResponse:
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    detail_url = {
        'moscow_legends': 'static/places/moscow_legends.json',
        'roofs24': 'static/places/roofs24.json',
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
                    "detailsUrl": detail_url[place_id]
                }
            }
        )
    return HttpResponse(
        loader.get_template('index.html').render({'geo_json': geo_json}, request)
    )
