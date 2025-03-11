from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import SessionDep
from app.models.session import Session, SessionCreate
from fastapi import HTTPException
from sqlmodel import select

router = APIRouter()

@router.post("/register")
def register(session: SessionCreate, db: SessionDep = Depends()):
    db_session = Session(
        patient_id=session.patient_id,
        psychologist_id=session.psychologist_id,
        audio_url=session.audio_url,
        transcript=session.transcript,
        analysis=session.analysis
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@router.get("/{session_id}")
def get_session(session_id: int, db: SessionDep = Depends()):
    session = db.exec(select(Session).where(Session.id == session_id)).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.delete("/{session_id}")
def delete_session(session_id: int, db: SessionDep = Depends()):
    db_session = db.exec(select(Session).where(Session.id == session_id)).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found")
    db.delete(db_session)
    db.commit()