from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    patient_id: int
    audio_url: str
