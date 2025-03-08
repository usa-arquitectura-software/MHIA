from fastapi import FastAPI
from app.routes import auth, users, patients, sessions,audio
from app.database import init_db
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager






@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_db()
    yield



app = FastAPI(title="Plataforma Psicólogos",lifespan=lifespan)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes (solo para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

# from fastapi import FastAPI, Depends, HTTPException
# from typing import List, Dict
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse, RedirectResponse
# # from sqlalchemy.orm import Session
# from sqlmodel import select
# from .models import PsycologistCreate, Psycologist, PsycologistLogin
# from .database import SessionDep, create_all_tables
# from .security import hash_password, verify_password
# from fastapi.middleware.cors import CORSMiddleware
# # from . import models, schemas
# # from .schemas import PsicologoCreate, PsicologoLogin, PsicologoOut

# # # Crear tablas en la base de datos
# # models.Base.metadata.create_all(bind=engine)

# app = FastAPI(lifespan= create_all_tables)

# # Allow all origins (for development) - Restrict in production!
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change to your frontend URL in production (e.g., ["http://localhost:3000"])
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
#     allow_headers=["*"],  # Allows all headers
# )

# # Montar carpeta 'static' para servir archivos estáticos
# app.mount("/static", StaticFiles(directory="app/static"), name="static")


# @app.get("/", response_class=RedirectResponse)
# def root():
#     return RedirectResponse("/login")


# # Ruta para servir index.html
# @app.get("/login", response_class=HTMLResponse)
# async def get_index():  
#     with open("app/static/index.html", "r") as f:
#         return HTMLResponse(content=f.read())
    
# # # Dependencia para obtener una sesión de base de datos en cada request
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# # 📌 Endpoint de registro
# @app.post("/register_psycologist", response_model=Psycologist)
# def create_psicologist(pyscologist_data: PsycologistCreate, session: SessionDep):

#     new_psycologyst = Psycologist.model_validate(pyscologist_data.model_dump())
#     new_psycologyst.password = hash_password(new_psycologyst.password)
#     session.add(new_psycologyst)
#     session.commit()

#     # db.refresh(nuevo_psicologo)
#     # Verificar si el email ya está registrado
#     # db_psicologo = db.query(Psicologo).filter(Psicologo.email == pyscologist_data.email).first()
#     # if db_psicologo:
#     #     raise HTTPException(status_code=400, detail= 'El correo ya existe')


#     # # Crear nuevo psicólogo
#     # nuevo_psicologo = Psicologo(
#     #     email = pyscologist_data.email,
#     #     name = pyscologist_data.name,        
#     #     password=pyscologist_data.password,
#     #     age=pyscologist_data.age
#     # )
#     # db.add(nuevo_psicologo)
#     # db.commit()
#     # db.refresh(nuevo_psicologo)
#     return new_psycologyst

# Incluir rutas
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(audio.router, prefix="/audio", tags=["Audio"])
#app.include_router(patients.router)
#app.include_router(sessions.router)


@app.get("/")
async def read_root():
    return {"message": "API funcionando. Ve a /static/index.html para la interfaz"}

# # 📌 Endpoint de login
# # @app.post("/login")
# # def login(login_data: schemas.PsicologoLogin, db: Session = Depends(get_db)):
# #     # Buscar al psicólogo por email
# #     psicologo = db.query(Psicologo).filter(Psicologo.email == login_data.email).first()
# #     if not psicologo: 
# #         raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
#     # # Verificar contraseña (en este ejemplo no está hasheada, ¡ojo en producción!)
#     # if psicologo.password != login_data.password:
#     #     raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     # return {"message": f"Welcome {psicologo.name}"}

# @app.post("/login_psycologist")
# def login_psycologist(login_data: PsycologistLogin, session: SessionDep):
#     # 1️⃣ Buscar al psicólogo por email
#     psycologist = session.exec(select(Psycologist).where(Psycologist.email == login_data.email)).first()
    
#     if not psycologist or not verify_password(login_data.password, psycologist.password):
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     return {"message": f"Welcome {psycologist.name}", "id": psycologist.id}


# @app.get("/psycologist", response_model=list[Psycologist])
# def list_psicologists(session:SessionDep):
#      return session.exec(select(Psycologist)).all()
