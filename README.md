### Описание:

Учебный проект api_yatube - это API социальной сети yatube.

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
python3 -m venv venv
```

```
source venv/bin/activate
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

POST-запрос с токеном, добавление новой публикации в коллекцию публикаций.

`POST http://localhost:port/api/v1/posts/`

```
{
    "username": "username",
    "password": "password"
}
```

Ответ:

```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTU5ODM3MiwianRpIjoiMjFhM2E3ZWNmYjQ4NGZmNzhkNWUxMDlmOTJlMjU0MjgiLCJ1c2VyX2lkI._BFxjdOwA-wIkjLkS1QOprdJDtlqnkxuHUy94mVGNkM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NTk4MzcyLCJqdGkiOiI3OGU4ZWMzOWU2MGM0ZjY0YmE1ZDI4OGM1ZjI1YjA5MSIsInVzZXJfaWQ.LZ2pzMOWTeshWX577MVMGJ34SjXu2-HFSKww6qWIGe8"
}
```
