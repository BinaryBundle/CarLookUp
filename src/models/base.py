from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from src.config import PSQL_DB_HOST, PSQL_DB_NAME, PSQL_DB_USER, PSQL_DB_PASSWORD


DATABASE_URL = f"postgresql+asyncpg://{PSQL_DB_USER}:{PSQL_DB_PASSWORD}@{PSQL_DB_HOST}/{PSQL_DB_NAME}"
Base = declarative_base()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

