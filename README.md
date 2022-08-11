# Проект API для Yatybe

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/vBaMnup/api_final_yatube)

### Описание
Api для сайта Yatube.
Сам сайт можно посмотреть тут: http://andryuxa.pythonanywhere.com/
### Возможности

- Регистрация
- Публикация
- Подписки 
- Комментарии
### Технологии

- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vBaMnup/api_final_yatube.git
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

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры использования:
Для получения списка постов (GET):
```
/api/v1/posts/
```
Добавить пост (POST):
```
/api/v1/posts/
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Другие примеры можно посмотреть по адресу /redoc/


### Автор
[Paskov Andrey](https://vk.com/andrey_paskov)
