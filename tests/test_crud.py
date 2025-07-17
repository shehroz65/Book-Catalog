import pytest, pytest_asyncio
from app import crud, schemas
from app.database import Base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


TEST_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture 
async def async_session():
    # Create an in-memory SQLite DB just for this test run
    engine = create_async_engine(TEST_DB_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    async with AsyncSessionLocal() as session:
        yield session
    await engine.dispose()

@pytest.mark.asyncio
async def test_create_and_get_book(async_session):
    # Test create_book and get_book functions
    book_in = schemas.BookCreate(title="UnitTest Book", author="Shehroz Test", published_year=2023)
    book = await crud.create_book(async_session, book_in)
    assert book.title == "UnitTest Book"

    fetched = await crud.get_book(async_session, book.id)
    assert fetched.id == book.id
    assert fetched.author == "Shehroz Test"

@pytest.mark.asyncio
async def test_update_book(async_session):
    # Create a book
    book_in = schemas.BookCreate(title="Before Update", author="Shehroz Khan", published_year=2020)
    book = await crud.create_book(async_session, book_in)

    # Update the book
    book_update = schemas.BookUpdate(title="After Update", author="Abdullah Khan", published_year=2021)
    updated_book = await crud.update_book(async_session, book, book_update)

    assert updated_book.title == "After Update"
    assert updated_book.published_year == 2021

@pytest.mark.asyncio
async def test_delete_book(async_session):
    # Create a book
    book_in = schemas.BookCreate(title="To Be Deleted", author="Ahmed Khan", published_year=2022)
    book = await crud.create_book(async_session, book_in)

    # Delete the book
    await crud.delete_book(async_session, book)

    # Try to get it again → should return None
    deleted = await crud.get_book(async_session, book.id)
    assert deleted is None
