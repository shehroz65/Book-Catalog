from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/books/", response_model=list[schemas.BookOut])
async def list_books(db: AsyncSession = Depends(get_db)):
    return await crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.BookOut)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/", response_model=schemas.BookOut)
async def create_book(book: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.BookOut)
async def update_book(book_id: int, book_update: schemas.BookUpdate, db: AsyncSession = Depends(get_db)):
    db_book = await crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return await crud.update_book(db, db_book, book_update)

@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    db_book = await crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    await crud.delete_book(db, db_book)
    return {"detail": "Book deleted"}