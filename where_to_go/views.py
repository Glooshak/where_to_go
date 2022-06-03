from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.template import loader


def show_main_page(
        request: HttpRequest,
) -> HttpResponse:
    return HttpResponse(
        loader.get_template('main.html').render({}, request)
    )
