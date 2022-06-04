from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.template import loader


geo_json = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "static/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "static/places/roofs24.json"
          }
        }
      ]
    }


def show_main_page(
        request: HttpRequest,
) -> HttpResponse:
    return HttpResponse(
        loader.get_template('index.html').render({'geo_json': geo_json}, request)
    )
