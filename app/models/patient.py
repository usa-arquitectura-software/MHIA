from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.user import User

class Patient(SQLModel, table=True):
    __tablename__ = "patients"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    psychologist_id: int = Field(foreign_key="users.id")

    psychologist: User = Relationship()
