# Restaurant Reservation API

## Описание проекта

Сервис для бронирования столиков в ресторане, реализованный с использованием FastAPI и PostgreSQL. API позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами.

## Функциональные требования

### Модели

1. **Table** – Столик в ресторане:
   - `id`: int
   - `name`: str (например, "Table 1")
   - `seats`: int (количество мест)
   - `location`: str (например, "зал у окна", "терраса")

2. **Reservation** – Бронь:
   - `id`: int
   - `customer_name`: str
   - `table_id`: int (FK на Table)
   - `reservation_time`: datetime
   - `duration_minutes`: int

### Методы API

#### Столики:

- `GET /tables/` — Получить список всех столиков
- `POST /tables/` — Создать новый столик
- `DELETE /tables/{id}` — Удалить столик

#### Брони:

- `GET /reservations/` — Получить список всех броней
- `POST /reservations/` — Создать новую бронь
- `DELETE /reservations/{id}` — Удалить бронь

### Логика бронирования

- Нельзя создать бронь, если в указанный временной слот столик уже занят (пересечение по времени и table_id).
- Бронь может длиться произвольное количество минут.
- Валидации обрабатываются на уровне API (например, конфликт брони должен выдавать ошибку с пояснением).

## Технические требования

- Используется FastAPI как основной фреймворк.
- Работа с БД через SQLAlchemy.
- Используется PostgreSQL.
- Alembic для миграций.
- Приложение обернуто в Docker.
- Используется docker-compose для запуска всех компонентов.
- Структура проекта модульная: `reservations/`, `tables/`, `dao/`.
- Код легко расширяемый.


## Установка и запуск

1. Убедитесь, что у вас установлены [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).

2. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/xolegx/reservation.git 
   cd app
   ```

3. Создайте файл `.env` в корне проекта и укажите настройки вашей базы данных:

   ```
   DB_USER=postgres
   DB_PASS=postgres
   ```

4. Запустите приложение с помощью Docker Compose:

   ```bash
   docker-compose up --build
   ```

5. После успешного запуска API будет доступно по адресу: `http://localhost:8000`.

