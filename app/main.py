from fastapi import FastAPI, Depends, HTTPException
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from .models import Psicologo
from .database import SessionLocal, engine
from . import models, schemas
from .schemas import PsicologoCreate, PsicologoLogin, PsicologoOut

# Crear tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Ruta para servir index.html
@app.get("/", response_class=HTMLResponse)
async def get_index():  
    with open("app/static/index.html", "r") as f:
        return HTMLResponse(content=f.read())
    
# Dependencia para obtener una sesión de base de datos en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📌 Endpoint de registro
@app.post("/register",response_model=PsicologoOut )
def register(psicologo_data: PsicologoCreate, db: Session = Depends(get_db)):
    # Verificar si el email ya está registrado
     db_psicologo = db.query(Psicologo).filter(Psicologo.email == psicologo_data.email).first()
     if db_psicologo:
         raise HTTPException(status_code=400, detail= 'El correo ya existe')
     
     # Crear nuevo psicólogo
     nuevo_psicologo = Psicologo(
         email = psicologo_data.email,
         name = psicologo_data.name,        
         password=psicologo_data.password,
         age=psicologo_data.age
     )
     db.add(nuevo_psicologo)
     db.commit()
     db.refresh(nuevo_psicologo)
     return nuevo_psicologo
    
             
    

# 📌 Endpoint de login
@app.post("/login")
def login(login_data: schemas.PsicologoLogin, db: Session = Depends(get_db)):
    # Buscar al psicólogo por email
    psicologo = db.query(Psicologo).filter(Psicologo.email == login_data.email).first()
    if not psicologo: 
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    # Verificar contraseña (en este ejemplo no está hasheada, ¡ojo en producción!)
    if psicologo.password != login_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": f"Welcome {psicologo.name}"}
