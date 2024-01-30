from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.database.config import settings_db


def get_connection() -> AsyncEngine:
    return create_async_engine(
        url=settings_db.database_url,
        echo=settings_db.POSTGRES_ECHO,
    )


try:
    engine = get_connection()
    Base = declarative_base()
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    print("Connection created successfully.")
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

# Base.metadata.create_all(engine)
