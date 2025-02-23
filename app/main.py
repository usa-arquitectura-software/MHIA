from fastapi import FastAPI, Depends, HTTPException
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
# from sqlalchemy.orm import Session
from sqlmodel import select
from .models import Psicologo, PsycologistCreate, Psycologist
from .database import SessionLocal, engine, SessionDep, create_all_tables
# from . import models, schemas
# from .schemas import PsicologoCreate, PsicologoLogin, PsicologoOut

# # Crear tablas en la base de datos
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan= create_all_tables)

# Montar carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=RedirectResponse)
def root():
    return RedirectResponse("/login")


# Ruta para servir index.html
@app.get("/login", response_class=HTMLResponse)
async def get_index():  
    with open("app/static/index.html", "r") as f:
        return HTMLResponse(content=f.read())
    
# # Dependencia para obtener una sesión de base de datos en cada request
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# 📌 Endpoint de registro
@app.post("/psycologists", response_model=Psycologist)
def create_psicologist(pyscologist_data: PsycologistCreate, session: SessionDep):

    new_psycologyst = Psycologist.model_validate(pyscologist_data.model_dump())
    new_psycologyst.id = 1
    session.add(new_psycologyst)
    session.commit()

    # db.refresh(nuevo_psicologo)
    # Verificar si el email ya está registrado
    # db_psicologo = db.query(Psicologo).filter(Psicologo.email == pyscologist_data.email).first()
    # if db_psicologo:
    #     raise HTTPException(status_code=400, detail= 'El correo ya existe')


    # # Crear nuevo psicólogo
    # nuevo_psicologo = Psicologo(
    #     email = pyscologist_data.email,
    #     name = pyscologist_data.name,        
    #     password=pyscologist_data.password,
    #     age=pyscologist_data.age
    # )
    # db.add(nuevo_psicologo)
    # db.commit()
    # db.refresh(nuevo_psicologo)
    return {
        "message": "Created Successfully a new Psicologist"
    }

             
    

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

@app.get("/psicologists", response_model=list[Psycologist])
def list_psicologists(session:SessionDep):
     session.exec(select(Psycologist)).all()