from fastapi import FastAPI, Depends, HTTPException
from models import User,LoginData
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir index.html
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())


FAKE_DB: List[Dict] = [
    {"email": "juan.perez@example.com", "name": "Juan Pérez", "password": "1234", "age": 28},
    {"email": "maria.gomez@example.com", "name": "María Gómez", "password": "pass123", "age": 24},
    {"email": "carlos.lopez@example.com", "name": "Carlos López", "password": "secure456", "age": 30},
    {"email": "ana.rodriguez@example.com", "name": "Ana Rodríguez", "password": "testpass", "age": 22},
    {"email": "david.martinez@example.com", "name": "David Martínez", "password": "david789", "age": 27},
]


# 📌 Servicio de autenticación
class AuthService:
    def __init__(self, db):
        self.db = db  # Referencia a la "base de datos"

    def register(self, user: User):
        # Verificar si el email ya existe
        if any(u["email"] == user.email for u in self.db):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Guardar usuario en la base de datos simulada
        self.db.append(user.model_dump())
        return {"message": "User registered successfully"}

    def login(self, login_data: LoginData):
        # Buscar usuario por email y password
        user = next((u for u in self.db if u["email"] == login_data.email and u["password"] == login_data.password), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": f"Welcome {user['name']}"}

# 📌 Inyección de dependencias (Retorna instancia de AuthService con la DB)
def get_auth_service():
    return AuthService(FAKE_DB)


# 📌 Endpoint de registro
@app.post("/register")
def register(user: User, service: AuthService = Depends(get_auth_service)):
    return service.register(user)

# 📌 Endpoint de login
@app.post("/login")
def login(login_data: LoginData, service: AuthService = Depends(get_auth_service)):
    return service.login(login_data)
