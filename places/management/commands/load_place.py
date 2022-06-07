from dataclasses import dataclass
from io import BytesIO

from django.core.management.base import BaseCommand, CommandError, CommandParser
import requests
from yarl import URL
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

from places.models import Place


PLACE = {
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}

PLACE_URL = 'https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'
# PLACE_URL = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'

'https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json' \
'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'


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
        # place_url = options.get('place_url')

        place_url = URL(PLACE_URL)
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
            images: list[JpegImageFile] = [
                Image.open(BytesIO(requests.get(image_url).content))
                for image_url in place_description.imgs
            ]
            obj, created = Place.objects.get_or_create(
                title=place_description.title,
                lng=place_description.coordinates.lng,
                lat=place_description.coordinates.lat,
                defaults={
                    'description_short': place_description.description_short,
                    'description_long': place_description.description_long,
                }
            )
            if created:
                # obj.image_set.create(picture=...)
                obj: Place
                for image in images:
                    obj.image_set.create(
                        picture=image
                    )

        except Exception as e:
            raise CommandError(
                f'There is an error {e.__repr__()} while fetching {place_url}'
            )

        pass
        # self.stdout.write(self.style.SUCCESS(f'{options}'))
