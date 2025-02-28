# models.py
# from sqlalchemy import Column, Integer, String
# from .database import Base
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
# class Psicologo(Base):
#     __tablename__ = 'psicologos'
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(255), unique=True, index=True, nullable=False)
#     name = Column(String(255), nullable=False)
#     password = Column(String(255), nullable=False)
#     age = Column(Integer, nullable=True)


# schemas.py

class PsycologistBase(SQLModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

class PsycologistCreate(PsycologistBase):
    name: str = Field(default=None)
    age: int = Field(default=None)

class Psycologist(PsycologistCreate, table=True):
    id: int | None = Field(default=None,primary_key =True)

class PsycologistLogin(PsycologistBase):
    pass