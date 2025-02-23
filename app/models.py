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
    name: str = Field(default=None)
    age: int = Field(defalult=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

# Datos necesarios para registrar un Psycologist
class PsycologistCreate(PsycologistBase):
    pass

# Esquema de salida (para evitar exponer password)
class Psycologist(PsycologistBase, table=True):
    id: int | None = Field(default=None,primary_key =True)
