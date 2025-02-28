from fastapi import FastAPI
from app.routes import auth, users, patients, sessions,audio
from app.database import Base, engine
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


# Inicializar la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Plataforma Psicólogos")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes (solo para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Incluir rutas
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(audio.router, prefix="/audio", tags=["Audio"])
#app.include_router(patients.router)
#app.include_router(sessions.router)


@app.get("/")
async def read_root():
    return {"message": "API funcionando. Ve a /static/index.html para la interfaz"}