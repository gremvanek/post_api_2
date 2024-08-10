# Проект API

Это проект Django REST API, использующий Django и Django REST Framework для создания и управления API. Документация API предоставляется через Swagger, и проект упакован с помощью Docker.

## Содержание

- [Проект API](#проект-api)
  - [Содержание](#содержание)
  - [Требования](#требования)
  - [Установка и запуск](#установка-и-запуск)
  - [Доступ к API](#доступ-к-api)
  - [Использование JWT для аутентификации](#использование-jwt-для-аутентификации)
  - [Документация API](#документация-api)
  - [Остановка](#остановка)

## Требования

1. [Docker](https://www.docker.com/get-started) (и [Docker Compose](https://docs.docker.com/compose/install/))
2. [Python 3.12+](https://www.python.org/downloads/)

## Установка и запуск

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Создайте и запустите контейнеры Docker:**

    ```bash
    docker-compose up --build
    ```

    Это создаст и запустит контейнеры для вашего приложения, базы данных PostgreSQL и Redis.

3. **Выполните миграции и создайте суперпользователя (если нужно):**

    Откройте новый терминал и выполните следующие команды:

    ```bash
    docker-compose exec app python manage.py migrate
    docker-compose exec app python manage.py createsuperuser
    ```

    Следуйте инструкциям на экране для создания суперпользователя.

## Доступ к API

После запуска контейнеров вы можете получить доступ к вашему API через браузер или инструмент для тестирования API, такой как Postman.

- **Swagger UI**: Перейдите по адресу [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) для просмотра и тестирования API через Swagger UI.

## Использование JWT для аутентификации

1. **Получите JWT токен:**

    Отправьте POST-запрос на [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/) с учетными данными пользователя (например, имя пользователя и пароль) для получения токена доступа и обновления.

    Пример запроса:

    ```bash
    curl -X POST http://127.0.0.1:8000/api/token/ -d '{"username":"your_username", "password":"your_password"}' -H "Content-Type: application/json"
    ```

2. **Используйте JWT токен для авторизации:**

    Включите токен в заголовок `Authorization` вашего запроса, добавив `Bearer` перед токеном.

    Пример запроса:

    ```bash
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://127.0.0.1:8000/your-protected-endpoint/
    ```

## Документация API

Документация API доступна по адресу [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/).

## Остановка

Чтобы остановить контейнеры, выполните:

```bash
docker-compose down
