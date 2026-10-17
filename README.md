# FastAPI Library API

[فارسی](#فارسی) | [English](#english)

---

## فارسی

### معرفی پروژه

این پروژه یک API ساده برای مدیریت کتاب‌ها با استفاده از **FastAPI** است. این سیستم امکان مشاهده، ثبت، ویرایش و حذف کتاب‌ها را فراهم می‌کند.

اطلاعات کتاب‌ها در یک متغیر پایتون ذخیره می‌شوند و برای اجرای پروژه نیازی به پایگاه داده نیست.

### امکانات

- دریافت فهرست کتاب‌ها
- افزودن کتاب جدید
- دریافت اطلاعات یک کتاب بر اساس شناسه
- تغییر عنوان یک کتاب
- حذف کتاب
- مدیریت کتاب‌های پیدا نشده با پاسخ HTTP 404

### پیش‌نیازها

- Python 3.10 یا بالاتر
- FastAPI

### نصب و راه‌اندازی

۱. مخزن را دریافت کنید:

```bash
git clone https://github.com/m-h-Khalifenajaf/fastapi-library-api.git
cd fastapi-library-api
```

۲. یک محیط مجازی بسازید:

```bash
python -m venv .venv
```

۳. محیط مجازی را در ویندوز فعال کنید:

```powershell
.venv\Scripts\Activate.ps1
```

۴. وابستگی‌های پروژه را نصب کنید:

```bash
pip install -r requirements.txt
```

### اجرای پروژه

دستور زیر را اجرا کنید:

```bash
fastapi dev main.py
```

آدرس اجرای API:

http://127.0.0.1:8000

مستندات تعاملی API:

http://127.0.0.1:8000/docs

### مسیرهای API

| متد HTTP | مسیر | توضیحات |
|---|---|---|
| GET | `/books` | دریافت فهرست عنوان کتاب‌ها |
| POST | `/books?title_new_book={title}` | افزودن کتاب جدید |
| GET | `/books/{id_book}` | دریافت اطلاعات یک کتاب |
| PATCH | `/books/{id_book}?title={title}` | تغییر عنوان کتاب |
| DELETE | `/books/{id_book}` | حذف کتاب |

### نحوه ذخیره‌سازی اطلاعات

اطلاعات کتاب‌ها در یک لیست پایتون در حافظه نگهداری می‌شوند. با توقف یا راه‌اندازی مجدد برنامه، اطلاعات به مقادیر اولیه بازمی‌گردند.

---

## English

### Project Description

This project is a simple **Library Management API** built with FastAPI. It provides endpoints to retrieve, create, update, and delete books.

Book data is stored in a Python list in memory, so no database is required.

### Features

- Retrieve all book titles
- Add a new book
- Retrieve a book by ID
- Update a book's title
- Delete a book
- Return HTTP 404 responses for books that do not exist

### Requirements

- Python 3.10 or higher
- FastAPI

### Installation

1. Clone the repository:

```bash
git clone https://github.com/m-h-Khalifenajaf/fastapi-library-api.git
cd fastapi-library-api
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Start the development server:

```bash
fastapi dev main.py
```

API base URL:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

### API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Retrieve all book titles |
| POST | `/books?title_new_book={title}` | Add a new book |
| GET | `/books/{id_book}` | Retrieve a book by ID |
| PATCH | `/books/{id_book}?title={title}` | Update a book's title |
| DELETE | `/books/{id_book}` | Delete a book by ID |

### Example Requests

Add a new book:

```http
POST /books?title_new_book=FastAPI
```

Retrieve a book by ID:

```http
GET /books/4
```

Example response:

```json
{
  "title": "FastAPI",
  "id": 4
}
```

If the requested book does not exist, the API returns an HTTP 404 response.

### Data Storage

Book information is stored in an in-memory Python list. All changes are lost when the application restarts.

### Project Purpose

This project was created for educational purposes to practice building APIs with FastAPI, working with HTTP methods, and implementing CRUD operations.
