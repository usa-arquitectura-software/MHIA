from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    psychologist_id = Column(Integer, ForeignKey("users.id"))
    session_date = Column(DateTime, default=datetime.utcnow)
    audio_url = Column(String, nullable=True)
    transcript = Column(Text, nullable=True)
    analysis = Column(Text, nullable=True)
    patient = relationship("Patient")
    psychologist = relationship("User")
