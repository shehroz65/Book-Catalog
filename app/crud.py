from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def get_books(db: AsyncSession):
    # Run SELECT query to get all Book records
    result = await db.execute(select(models.Book))
    # Extract all rows as a list of model instances
    return result.scalars().all()

async def get_book(db: AsyncSession, book_id: int):
    # Run SELECT query for a single Book by ID
    result = await db.execute(select(models.Book).where(models.Book.id == book_id))
    # Get one result or None if no match
    return result.scalar_one_or_none()

async def create_book(db: AsyncSession, book: schemas.BookCreate):
    # Create Book SQLAlchemy model from Pydantic schema
    db_book = models.Book(**book.model_dump())
    # Add to session (marks it for insertion)
    db.add(db_book)
    # Commit transaction to persist changes
    await db.commit()
    # Refresh instance to get updated data, so auto generated fields (like ID) are updated in the Python object
    await db.refresh(db_book)
    return db_book


async def update_book(db: AsyncSession, db_book: models.Book, book_update: schemas.BookUpdate):
    # Update model fields with new data
    for key, value in book_update.model_dump().items():
        setattr(db_book, key, value)
    # Commit transaction to save changes
    await db.commit()
    # Refresh instance to get updated data, so auto generated fields (like ID) are updated in the Python object
    await db.refresh(db_book)
    return db_book


async def delete_book(db: AsyncSession, db_book: models.Book):
    # Mark instance for deletion
    await db.delete(db_book)
    # Commit transaction to apply deletion
    await db.commit()
