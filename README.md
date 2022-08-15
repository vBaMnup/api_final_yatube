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

``` bash
git clone git@github.com:vBaMnup/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

``` bash
python3 -m venv venv
```

``` bash
source venv/bin/activate
```

``` bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

``` bash
pip install -r requirements.txt
```

Выполнить миграции:

``` bash
python3 manage.py migrate
```

Запустить проект:

``` bash
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
``` json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Другие примеры можно посмотреть по адресу /redoc/


### Автор
[Paskov Andrey](https://vk.com/andrey_paskov)
