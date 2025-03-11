from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

# Base schema for user data
class UserBase(SQLModel):
    email: EmailStr
    username: str = Field(unique=True, index=True)

# Schema for user creation
class UserCreate(UserBase):
    password: str
    name: str
    age: Optional[int] = None
    role: str = Field(default="psicologo")

# Main User model for database
class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    hashed_password: str
    name: str
    age: Optional[int] = None
    role: str = Field(default="psicologo")

# Schema for login
class UserLogin(SQLModel):
    email: EmailStr
    password: str
