from pydantic import EmailStr, BaseModel


class User(BaseModel):
    nome: str 
    email: EmailStr 
    senha: str
    role: str

class Mesa(BaseModel):
    numero: int
    capacidade: int
    status: str