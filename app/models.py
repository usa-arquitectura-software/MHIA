# models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Psicologo(Base):
    __tablename__ = 'psicologos'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)

