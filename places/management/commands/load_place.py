from dataclasses import dataclass
from io import BytesIO
from uuid import uuid4

import requests
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from yarl import URL

from places.models import Place


@dataclass
class Coordinates:
    lng: str
    lat: str


@dataclass
class PlaceDescription:
    title: str
    imgs: list[str]
    description_short: str
    description_long: str
    coordinates: Coordinates


class Command(BaseCommand):

    help = 'Upload new places to the databases from json file'
    RAW_PLACE_URL_HOST = 'raw.githubusercontent.com'

    def add_arguments(
            self,
            parser: CommandParser,
    ) -> None:
        parser.add_argument(
            'place_url', type=str,
        )

    def handle(self, *args, **options) -> None:

        place_url = URL(options.get('place_url'))
        if place_url.host != self.RAW_PLACE_URL_HOST:
            place_url = URL.build(
                scheme=place_url.scheme,
                host=self.RAW_PLACE_URL_HOST,
                path=place_url.path.replace('/blob', ''),
            )
        try:
            resp = requests.get(place_url.__str__())
            resp.raise_for_status()
            json_resp = resp.json()
            place_description = PlaceDescription(
                title=json_resp['title'],
                imgs=json_resp['imgs'],
                description_short=json_resp['description_short'],
                description_long=json_resp['description_long'],
                coordinates=Coordinates(
                        lat=json_resp['coordinates']['lat'],
                        lng=json_resp['coordinates']['lng']
                    ),
            )
            raw_images: list[BytesIO] = [
                BytesIO(requests.get(image_url).content)
                for image_url in place_description.imgs
            ]
            place_obj, created = Place.objects.get_or_create(
                title=place_description.title,
                lng=place_description.coordinates.lng,
                lat=place_description.coordinates.lat,
                defaults={
                    'description_short': place_description.description_short,
                    'description_long': place_description.description_long,
                }
            )
            if created:
                place_obj: Place
                for raw_image in raw_images:
                    name = f'{place_obj.title}_{uuid4().__str__()}.jpg'
                    image_object = place_obj.image_set.create(
                        picture=name
                    )
                    image_object.picture.save(
                        name, raw_image, save=True
                    )

        except Exception as e:
            raise CommandError(
                f'There is an error {e.__repr__()} while fetching {place_url}'
            )

        self.stdout.write(
            self.style.SUCCESS(f'Place {place_obj.title} has been successfully uploaded!')
        )
