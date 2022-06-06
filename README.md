# Сервис по типу "Яндекс афиша" (одно из учебных заданий образовательного портала Devman)

# Задача, с которой сервис должен справлять
Артём просто обожает активный отдых. Это очень сочетается с его работой: он популярный блогер и регулярно рассказывает о своих мини-путешествиях на камеру. Иногда это посещение музеев и выставок, а иногда просто красивая дверь или урна.

Постоянный поиск “чем заняться” породил у Артёма целую кучу знаний о досуге в своём городе: по пятницам вечером можно встретить футболистов в соседнем дворе, а по вторникам репетиции маленького камерного театра, куда пускают всех желающих. Артём не просто посетил все местные леса и парки: в каждом он знает хорошие поляны для пикников, для сбора грибов, а где-то даже нашлись хорошие фоны для портретов.

Артём поделился со своими читателями всем, что знает сам, но вдруг его осенило: а что, если показать все эти места на карте? Людям легко читать о каких-то местах со своих мониторов и думать “да, сходить бы туда”, но если я покажу им, сколько замечательных мест и развлечений есть прямо возле их дома или работы – это может повлиять куда сильнее!

Артём хочет создать интерактивную карту Москвы, на которой будут все известные ему виды активного отдыха с подробными описаниями и комментариями. Яндекс.Афиша занимается чем-то похожим, но это бездушный робот, собирающий всё подряд. Она никогда не обратит внимание на красивый канализационный люк или отвратительную вывеску.

Карте быть, и Артём уже начал поиск энтузиастов, которые помогут с контентом. Параллельно идёт сбор команды для разработки сайта. Это будет большой проект и вам посчистливилось поучаствовать в нём с самого начала. Картой займётся фронтендщик, а вам предстоит:

    Создать Django-проект
    Сделать API с данными от Артёма
    Сделать админку максимально удобной для заполнения

# Демо
![docs/devman.gif](devman.gif)

# Запуск проекта
- Перед установкой убедитесь, что у вас есть python версии 3.10 и выше, а также инструмент менеджмента питоновских пакетов poetry (https://python-poetry.org/docs/)
- Клонируйте репозиторий к себе.
- Зайдите в директорию с проектом `cd where_to_go`
- В корневой директории проекта создайте файл `.env` и заполните его по примеру файла `.env-example`
- Выполните список комманд, представленный ниже.
- `poetry install --no-dev --no-root` установка зависимостей
- `poetry shell` активация виртуального окружения
- `python manage.py migrate` - запуск миграция
- `python manage.py createsuperuser` - создания учетки для админки
- `python manage.py runserver` - запуск приложения на дев сервере
# Добавление контента
Добавить контент можно через админку - воспользуйтесь учеткой, которую вы получили на шаге создания `superuser`.