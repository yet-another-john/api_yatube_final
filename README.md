### Описание:

Учебный проект api_yatube - это API социальной сети YaTube.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:yet-another-john/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

#### Примеры запросов:

GET-запрос, получение публикаций.

`GET http://127.0.0.1:8000/api/v1/posts`

```
Ответ:

[
    {
        "id": 1,
        "author": "lenovo",
        "text": "1",
        "pub_date": "2024-05-12T12:38:50.337464Z",
        "image": null,
        "group": null
    }
]
```
