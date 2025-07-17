# 📚 Book Catalog API

A FastAPI CRUD API to manage a book catalog, with async endpoints, SQLAlchemy (SQLite), and full test coverage.

## 🚀 Features

✅ Create, read, update, delete books  
✅ Async endpoints with FastAPI  
✅ SQLAlchemy ORM with SQLite  
✅ Pydantic validations  
✅ Unit + integration tests  
✅ Dockerized setup

## 🛠️ Setup (local)

1️⃣ Clone repo:

```bash
git clone https://github.com/shehroz65/Book-Catalog.git
cd Book-Catalog
```

2️⃣ Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Run app:

```bash
uvicorn app.main:app --reload
```

Open API docs: http://127.0.0.1:8000/docs

## 🐳 Setup with Docker

1️⃣ Build Docker image:

```bash
docker build -t book-catalog .
```

2️⃣ Run container:

```bash
docker run -p 8000:8000 book-catalog
```

App runs at: http://localhost:8000

## 🧪 Run Tests

✅ Run all tests:

```bash
pytest -v
```

✅ Run only unit tests:

```bash
pytest tests/test_crud.py -v
```

✅ Run only integration tests:

```bash
pytest tests/test_api.py -v
```

✅ Explanation:
- `-v` → verbose mode, shows details.

Logs will appear in the test output for easy tracking.

## 🔧 Run Full Flow Script
I have provided a ready-to-use shell (and .bat) script to test the entire CRUD flow via cURL.

1️⃣ Make it executable:

# chmod +x test_flow.sh

2️⃣ Run it:

# ./test_flow.sh 

Or for Windows, just run the .bat file
✅ This script:

Deletes all books.

Creates Book One

Lists books

Updates Book One

Creates Book Two

Lists books

Deletes Book One

Lists books (to check only Book Two remains)

⚠ Requirements:

FastAPI server running (uvicorn app.main:app --reload)

Python installed (for JSON parsing in the script)

## ⚡ Notes

- Database: SQLite file (`books.db`), auto-created.
- On startup, tables are auto-created.
- On shutdown, DB engine closes cleanly.

## Done by Shehroz Khan

Carefully written code to make sure no deprecation warnings are shown and latest event handlers, methods, coding styles are used. 
