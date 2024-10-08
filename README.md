
# Post API

  

Post API — это RESTful API на базе Django, позволяющее пользователям создавать посты и комментировать их. Проект использует Docker для контейнеризации, Celery для асинхронной обработки задач и Swagger для документирования API.

  

## Функционал

  

- Создание, чтение, обновление и удаление пользователей, постов и комментариев

- Валидация данных

- Административная панель для управления постами

- Документация API с использованием Swagger

  

## Технические требования

  

- Python 3.8+

- Django 3+

- Django REST Framework 3.10+

- PostgreSQL 10+

  

## Установка

  

1. Клонируйте репозиторий:

```bash
git clone https://github.com/вашпользователь/post_api_2.git
```
2. Создайте файл .env в корневой директории проекта со следующими переменными окружения: 
```bash
POSTGRES_DB=ваше_имя_бд

POSTGRES_USER=ваш_пользователь_бд

POSTGRES_PASSWORD=ваш_пароль_бд

SECRET_KEY=ваш_секретный_ключ_данджано
```
3. Постройте и запустите контейнеры:
```bash
docker-compose up --build
```
- Эта команда построит образы Docker и запустит все сервисы, определённые в файле docker-compose.yml.

  

## Структура приложения

## Задача 1: Модели

- Модель пользователя (User):

	- логин

	- пароль (минимум 8 символов, должен включать цифры)

	- номер

	- дата рождения (проверка возраста пользователя при создании поста)

	- дата создания

	- дата редактирования

  

- Модель поста (Post):

	- заголовок (проверка на запрещённые слова: ерунда, глупость, чепуха)

	- текст

	- изображение (если есть)

	- автор (ссылка на пользователя)

	- комментарии (связь с комментариями)

	- дата создания

	- дата редактирования  

- Модель комментария (Comment):

	- автор (ссылка на пользователя)

	 - текст

	- дата создания

	- дата редактирования

  

## Задача 2: Эндпоинты

  

- Пользователь (User):

	- CREATE: Регистрация пользователей.

	- READ: Администратор/авторизованные пользователи.

	- UPDATE: Администратор/пользователь может редактировать только себя.

	- DELETE: Администратор.

  

- Пост (Post):

	- CREATE: Авторизованные пользователи.

	- READ: Все пользователи.

	- UPDATE: Администратор/пользователь может редактировать только свои посты.

	- DELETE: Администратор/пользователь может удалять свои посты.

  

- Комментарий (Comment):

	- CREATE: Авторизованные пользователи.

	- READ: Все пользователи.

	- UPDATE: Администратор/пользователь может редактировать только свои комментарии.

	- DELETE: Администратор/пользователь может удалять свои комментарии.

  

## Задача 3: Валидаторы

  

- Модель пользователя (User):

	- Валидатор для пароля (минимум 8 символов, должен включать цифры).

	- Валидатор для почты (разрешены домены: mail.ru, yandex.ru).

  

- Модель поста (Post):

	- Проверка возраста автора поста (достиг 18 лет).

	- Проверка заголовка на запрещённые слова: ерунда, глупость, чепуха.

  

## Задача 4: Админ. панель

  

- Добавлена ссылка на автора в объекте поста.

- Добавлен фильтр по дате создания поста.

  

## Доступ к приложению

  

Django приложение будет доступно по адресу:

  
```bash
http://localhost:8000
```
  
## Swagger
Интерфейс Swagger для документации API доступен по адресу:

  
  
```bash
http://localhost:8000/swagger/
```
  

## Запуск Celery

  

- Celery используется для обработки асинхронных задач в фоновом режиме.Рабочий процесс Celery автоматически запускается с командой docker-compose up.

  

	- Если нужно запустить рабочий процесс Celery вручную:
	```bash
		docker-compose run --rm celery
	```  

	- Если нужно запустить планировщик Celery beat вручную:
	```bash
		docker-compose run --rm celery-beat
	``` 

  

## Запуск миграций

  

- Для применения миграций:  
	```bash
		docker-compose exec app python3 manage.py migrate
	```  

- Если нужно создать новые миграции:
	```bash
		docker-compose exec app python3 manage.py makemigrations
	```
## Остановка приложения

  

- Чтобы остановить приложение и удалить все контейнеры:
	```bash
		docker-compose down
	```
## Содействие  

- Если вы хотите внести свой вклад в этот проект, пожалуйста, сделайте форк репозитория и отправьте пулл-реквест. README.MD сделан при помощи Stackedit. https://github.com/benweet/stackedit
