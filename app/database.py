from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./books.db"

# Create async engine; echo=True logs SQL queries for debugging
engine = create_async_engine(DATABASE_URL, echo=True)

"""
SessionLocal: Factory for creating AsyncSession instances.

- expire_on_commit=False keeps ORM objects in memory after commit(), avoiding automatic expiration.
- This allows access to object attributes without triggering additional SELECT queries.
- IMPORTANT: If you need to retrieve database-side updates (e.g., auto-generated IDs, timestamps, triggers),
  you must explicitly call db.refresh(obj) after committing.
"""
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Base class for ORM models (used to define tables)
Base = declarative_base()
