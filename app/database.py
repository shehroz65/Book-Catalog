from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./books.db"

# Create async engine; echo=True logs SQL queries for debugging
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory using AsyncSession; expire_on_commit=False keeps objects active after commit (to not trigger an extra SELECT query after db.commit())
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
# If expire_on_commit=False, we dont need to do db.refresh() after commit to get updated data, as the object remains active.

# Base class for ORM models (used to define tables)
Base = declarative_base()
