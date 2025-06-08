from pydantic import EmailStr, BaseModel


class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    role: str