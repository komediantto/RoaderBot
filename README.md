# RoaderBot

## Описание

Telegram-бот с админкой для краевой администрации, помогает принимать жалобы на убитые дороги в Северной Осетии.

## Технологии

Django, Aiogram, Rest API, DRF, PostgreSQL, docker

## Как запустить

Создать .env файл в корне проекта вида:

```env
BOT_TOKEN = <ваш токен>
DEBUG = <True или False>
HOST = <свой хост, либо *>
SECRET_KEY = <свой secret key django>
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = postgres
DB_HOST = db
DB_PORT = 5432
```

Из корневой директории запустить docker-compose

```bash
docker-compose up -d
```

При первом запуске требуется наполнить БД данными о дорогах, для этого идём в контейнер с Django

```bash
docker exec -it roaderbot-web-1 bash
```

Переходим в директорию app и запускаем скрипт

```bash
cd app
python manage.py runscript migrate_data_frov_xlsx
```

И заодно создадим суперюзера
```bash
python manage.py createsuperuser
```

Админка будет доступна по адресу http://0.0.0.0:8000/admin.

Бот запускается по команде /start и далее доступны следующие опции:
1. Пожаловаться на плохую дорогу
2. Оценить качество ремонта
3. Отправить предложение

##  Скриншоты бота

*начало*
![photo_2023-06-21_13-02-23](https://github.com/komediantto/RoaderBot/assets/62796239/4779c504-070a-4c6e-a7e7-f34b4e2df4da)


*регистрация*
![photo_2023-06-21_13-02-32](https://github.com/komediantto/RoaderBot/assets/62796239/2f085e3e-62af-4ea7-920c-ba4bcf4e9cb7)


*реализация отправки номера*
![photo_2023-06-21_13-02-37](https://github.com/komediantto/RoaderBot/assets/62796239/c8071695-14f1-4e3c-babb-c5bd0562fedb)


*опции*
![photo_2023-06-21_13-02-41](https://github.com/komediantto/RoaderBot/assets/62796239/5d237484-117b-4f70-9cef-95ffe52f47e0)

![photo_2023-06-21_13-02-43](https://github.com/komediantto/RoaderBot/assets/62796239/88d9002b-5481-4b57-a7f3-7a6f36004764)


*выбор улицы*
![photo_2023-06-21_13-02-46](https://github.com/komediantto/RoaderBot/assets/62796239/bf7cc61a-3dd4-4ec3-b445-dd7aab867c3d)

##  Скриншоты админки

*населённые пункты*
![Снимок экрана от 2023-06-21 13-06-26](https://github.com/komediantto/RoaderBot/assets/62796239/07dc53c7-c61a-4b46-ad8f-77d571e9d4a2)


*оценки*
![Снимок экрана от 2023-06-21 13-08-48](https://github.com/komediantto/RoaderBot/assets/62796239/5213b8eb-1dcb-443b-a41e-56289bbb54c5)


*жалобы*
![Снимок экрана от 2023-06-21 13-08-59](https://github.com/komediantto/RoaderBot/assets/62796239/be9d0107-8b02-494b-b35e-5e919f00c414)


*улицы*
![Снимок экрана от 2023-06-21 13-09-06](https://github.com/komediantto/RoaderBot/assets/62796239/b358a9dd-0cbb-423a-8178-54b76c3faf2a)


*предложения*
![Снимок экрана от 2023-06-21 13-09-14](https://github.com/komediantto/RoaderBot/assets/62796239/c64977c1-7b62-4b2f-bc64-85c1f112160d)

