from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import SessionDep
from app.models.user import User, UserCreate
from app.services.auth import get_password_hash

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: SessionDep = Depends()):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        name=user.name,
        age=user.age,
        role=user.role
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "User registered successfully"}
