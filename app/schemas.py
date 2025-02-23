# # schemas.py
# from pydantic import BaseModel, EmailStr

# # Datos necesarios para registrar un Psicologo
# class PsicologoCreate(BaseModel):
#     email: EmailStr
#     name: str
#     password: str
#     age: int

# # Datos usados en el login
# class PsicologoLogin(BaseModel):
#     email: EmailStr
#     password: str

# # Esquema de salida (para evitar exponer password)
# class PsicologoOut(BaseModel):
#     id: int
#     email: str
#     name: str
#     age: int

#     class Config:
#         from_attributes = True  # Permite devolver objetos ORM directamente
