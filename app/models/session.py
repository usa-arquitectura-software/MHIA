from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.patient import Patient
from app.models.user import User

class Session(SQLModel, table=True):
    __tablename__ = "sessions"

    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patients.id")
    psychologist_id: int = Field(foreign_key="users.id")
    session_date: datetime = Field(default_factory=datetime.utcnow)
    audio_url: Optional[str] = None
    transcript: Optional[str] = None
    analysis: Optional[str] = None

    patient: Patient = Relationship()
    psychologist: User = Relationship()
