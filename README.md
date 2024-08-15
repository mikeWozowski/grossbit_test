## Тестовое задание для Python разработчика в Гроссбит

Этот проект представляет собой API для генерации кассовых чеков в формате PDF и создания QR-кодов, которые содержат ссылки на эти PDF-файлы.

## Установка и Запуск

### 1. Клонируйте репозиторий

```bash
https://github.com/mikeWozowski/grossbit_test.git
cd grossbit_test
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Настройте переменные окружения

Создайте файл `.env` в корневом каталоге проекта и добавьте в него настройки:

```env
DATABASE_NAME=db_name
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Примените миграции

```bash
python manage.py migrate
```

### 6. Запустите сервер

```bash
python manage.py runserver http://your_addres:8000
```

API будет доступен по адресу `http://your_addres:8000/`.

## API Эндпоинты

### `POST /cash_machine/`

- **Описание**: Генерирует PDF чек, создает QR-код с ссылкой на PDF и возвращает URL QR-кода.
- **Тело запроса**:
  ```json
  {
    "items": [1, 2, 3]  // Список ID товаров
  }
  ```
- **Ответ**:
  ```json
  {
    "qr_url": "http://your_address/media/qr_code.png"
  }
  ```

## Зависимости

Содержатся в файле `requirements.txt`:

```
Django==4.0.0
djangorestframework==3.14.0
pdfkit==1.0.0
qrcode==7.3.1
```
