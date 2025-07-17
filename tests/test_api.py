import logging
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
logging.basicConfig(level=logging.INFO)

def test_full_flow():
    # 1️⃣ Create book 1
    res1 = client.post("/books/", json={
        "title": "Book One",
        "author": "Shehroz First",
        "published_year": 2020
    })
    assert res1.status_code == 200
    book1 = res1.json()
    logging.info(f"Created Book1: {book1}")

    # 2️⃣ Get all books, check Book1 exists
    res2 = client.get("/books/")
    books = res2.json()
    assert any(b['id'] == book1['id'] for b in books)
    logging.info(f"Books after first create: {books}")

    # 3️⃣ Update Book1
    res3 = client.put(f"/books/{book1['id']}", json={
        "title": "Book One Updated",
        "author": "Shehroz",
        "published_year": 2021,
        "summary": "Updated summary"
    })
    assert res3.status_code == 200
    updated_book1 = res3.json()
    assert updated_book1['title'] == "Book One Updated"
    logging.info(f"Updated Book1: {updated_book1}")

    # 4️⃣ Create book 2
    res4 = client.post("/books/", json={
        "title": "Book Two",
        "author": "Shehroz Second Test",
        "published_year": 2022
    })
    assert res4.status_code == 200
    book2 = res4.json()
    logging.info(f"Created Book2: {book2}")

    # 5️⃣ Get all books, check both exist
    res5 = client.get("/books/")
    books = res5.json()
    assert len(books) >= 2
    logging.info(f"Books after second create: {books}")

    # 6️⃣ Delete Book1
    res6 = client.delete(f"/books/{book1['id']}")
    assert res6.status_code == 200
    logging.info(f"Deleted Book1 id: {book1['id']}")

    # 7️⃣ Get all books, check Book1 is gone
    res7 = client.get("/books/")
    books = res7.json()
    ids = [b['id'] for b in books]
    assert book1['id'] not in ids
    assert book2['id'] in ids
    logging.info(f"Books after deletion: {books}")
