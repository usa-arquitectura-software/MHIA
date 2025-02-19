from pydantic import BaseModel

class User(BaseModel):
    email: str
    name: str
    password: str
    age: int

# 📌 Modelo para el login
class LoginData(BaseModel):
    email: str
    password: str