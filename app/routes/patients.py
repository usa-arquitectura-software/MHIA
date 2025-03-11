from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import SessionDep
from app.models.patient import Patient, PatientCreate
from fastapi import HTTPException
from sqlmodel import select

router = APIRouter()

@router.post("/register")
def register(patient: PatientCreate, db: SessionDep = Depends()):
    db_patient = Patient(
        name=patient.name,
        email=patient.email,
        psychologist_id=patient.psychologist_id
    )  
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: SessionDep = Depends()):
    patient = db.exec(select(Patient).where(Patient.id == patient_id)).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}")
def update_patient(patient_id: int, patient: PatientCreate, db: SessionDep = Depends()):
    db_patient = db.exec(select(Patient).where(Patient.id == patient_id)).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_patient.name = patient.name
    db.commit()
    db.refresh(db_patient)