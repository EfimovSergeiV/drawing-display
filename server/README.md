# API

## Base URL
http://`hostname.local or 192.168.x.x`:8080

---

**URL:** `/drawings/list/`
- **Методы:** `GET`, `POST`, `PUT`, `DELETE`

---

### Получение всех объектов

**Запрос:**

- **Method:** `GET`

**Ответ:**
- **Status Code:** `200 OK`
- **Content type:** `application/JSON`
```JSON
[
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": "*string",
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": "*string",
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
]

```

**Параметры ответа:**
| Параметр    | Тип     | Обязательный | Генерируется   | Описание                           |
|-------------|---------|--------------|----------------|------------------------------------|
| `uuid`      | `str`   | Нет          | Да             | Уникальный идентификатор документа |
| `name`      | `str`   | Нет          | Да             | Отображаемое название документа    |
| `status`    | `str`   | Нет          | Да             | Статус объекта                     |
| `created_at`| `str`   | Нет          | Да             | Дата создания                      |
| `link`      | `str`   | Нет          | Нет            | Ссылка на PDF в хранилище          |
| `pdf`       | `str`   | Да           | Нет            | Путь до PDF документа              |
| `webp`      | `str`   | Нет          | Да             | Путь до изображения                |
| `webp_size` | `obj`   | Нет          | Да             | Размер изображения в пикселях      |
| `prw`       | `str`   | Нет          | Да             | Путь до изображения превью         |





### Запись новых объектов

**Запрос:**
- **Method:** `POST`
- **Content type:** `multipart/form-data`


| Поле    | Тип            | Обязательный | Описание                               |
|---------|----------------|--------------|----------------------------------------|
| `files` | `file[] (PDF)` | Да           | Список PDF-файлов для загрузки.        |


**Ответ:**
- **Status Code:** `201 CREATED`, `400 BAD_REQUEST`
- **Content type:** `application/JSON`

```JSON
[
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": "*string",
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": "*string",
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
]
```



### Обновление статуса объекта

**Запрос:**

- **Method:** `PUT`

```JSON
{
    "uuid": "string",
    "status": "completed",
}
```

**Ответ:**
- **Status Code:** `200 OK`, `404 NOT_FOUND`
- **Content type:** `application/JSON`

```JSON
{
    "uuid": "string",
    "name": "string",
    "status": "completed",
    "completed_at": "string"
}
```



### DELETE
Удаление объекта из базы данных

**Запрос:**

- **Method:** `DELETE`


**Ответ:**
- **Status Code:** `200 OK`, `404 NOT_FOUND`
- **Content type:** `application/JSON`

```JSON
{
    "uuid": "string"
}
```
