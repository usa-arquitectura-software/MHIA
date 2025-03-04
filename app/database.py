
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL
from app.models import Base

# Crear el motor asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear la sesión asíncrona
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Dependencia de sesión para FastAPI
async def get_db():
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# from sqlmodel import Session, create_engine, SQLModel
# from typing import Annotated
# from fastapi import Depends, FastAPI

# sqlite_name = "db.sqlite3"
# sqlite_url = f"sqlite:///./{sqlite_name}"


# engine = create_engine(sqlite_url)

# def create_all_tables(app: FastAPI):
#     SQLModel.metadata.create_all(engine) 
#     yield

# def get_session():
#     with Session(engine) as session:
#         yield session
        
# SessionDep = Annotated[Session, Depends(get_session)]

# # # database.py
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker, declarative_base

# # # URL de conexión para SQLite local (archivo "test.db" en la carpeta actual)
# # SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# # engine = create_engine(
# #     SQLALCHEMY_DATABASE_URL,
# #     connect_args={"check_same_thread": False}  # Solo necesario para SQLite
# # )
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # Base = declarative_base()

